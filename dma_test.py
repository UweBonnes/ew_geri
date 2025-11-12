# Scan all configured fiber port. Enable DMA hits for some time either
# sequential on all found downlinks or the downlink selected as first
# command line argument

# Receive the hits e.g. with wzdaq_app_geri x with x the fiber port to watch

import sys
import time
import agwb
import geri

import logging as log
log.basicConfig(format='%(filename)s:%(lineno)d - %(message)s')

g=geri.Geri()
g.init()

def get_efuse(smx):
    try:
        value = []
        for i in range(8):
            smx.write(192, 32, 128 + i)
            value.append(smx.read(192, 33) & 0xff)
            smx.write(192, 32, 0)
        efuse = "%02x%02x%02x%02x%02x%02x%02x%02x" % (
            value[7], value[6], value[5], value[4],
            value[3], value[3], value[1], value[0])
        return efuse
    except:
        return "Efuse failed"

keep_running = True
if len(sys.argv) >= 2:
  print("Testing only uplink(s) %d" % int(sys.argv[1]))
for port in range(agwb.NR_CROB1):
  if not keep_running:
    sys.exit()
  print("Testing port %d" % port)
  try:
    g.gbtfpga[port].init(attempts=20)
  except Exception as e:
    print("Fiber link %d not usable" % port)
    continue
  time.sleep(1)

  print(g.gbtfpga[port].gbtfpga_get_link_status())

  for i in range(10):
    # sometimes the first operation fails...
    # TODO: identify and fix the problem
    try:
      ver=g.gbtfpga[port].emu_regs.VER.read()
      id=g.gbtfpga[port].emu_regs.ID.read()
      if ver == 0 or id == 0:
        continue
      print(f"Port {port} Read GBTxEMU firmware ID: 0x{id:08x} and VER: 0x{ver:08x}")
      print(f"Success after {i} tries")
      break
    except Exception as e:
      if i < 9:
        pass
      else:
        print("Fiber communication failed\n")
        sys.exit()
    else:
      print("Didn't work!")
      sys.exit()

  se=g.scan_setup(port)
  if se == []:
      print("Running scan_setup() in tight loop.")
  while se == [] and keep_running:
      print(".", end = "",flush = True)
      se=g.scan_setup(port)
  for s in se:
    print("Characterizing Downlink: {}, Uplinks: {}".format(s.downlink, s.uplinks))
    s.characterize_clock_phase()
    s.initialize_clock_phase()
    s.characterize_data_phases()
    s.initialize_data_phases()
    s.scan_smx_asics_map()
    for s in se:
      s.synchronize_elink()
      s.hctsp_uplink.set_uplinks_mask()
      s.write_smx_elink_masks()

  import smx
  smxes = []
  for s in se:
    sxs = smx.smxes_from_setup_element(s)
    smxes.extend(sxs)
  print("Setup scan results:\n{}".format(se))
  while keep_running:
    for sx0 in smxes:
      if (len(sys.argv) < 2 or int(sys.argv[1]) == sx0.uplinks[0]) and keep_running:
        print("Testing Chip %s Uplink %d: " % (get_efuse(sx0), sx0.uplinks[0]), end = "")
        retries = 10
        n = 0
        old_writes = sx0.writes
        old_serror = sx0.one_retry
        old_merror = sx0.retries
        while n < retries:
          try:
            sx0.refclk_frq=80e6
            sx0.write(192,3,0xc)
            sx0.write(192,14,0)
            sx0.write(192,15,0xff)
            #Enable test hits
            sx0.write(192,19,0x3ff)
            sx0.write(192,18,2)
            #Configure generation of packet every 0.1 second
            g.regs.datapath.triv_proc.pkt_duration.write(4000000)
            #Start DMA
            g.regs.datapath.triv_proc.ctrl.reset.writef(1)
            time.sleep(0.1)
            g.regs.datapath.triv_proc.ctrl.reset.writef(0)
            time.sleep(0.1)
            g.regs.datapath.triv_proc.ctrl.run.writef(1)
            time.sleep(3)
            #Disble test hits
            sx0.write(192,15,0)
            sx0.write(192,3,0)
            #Stop DMA
            g.regs.datapath.triv_proc.ctrl.run.writef(0)
    
          except Exception as e:
            print(".", end = "")
            n = n + 1
            if n < retries:
              continue
            else:
              print(" Uplink %d failed after %d retries" % (sx0.uplinks[0], n), end = "")
              n = 0
          except KeyboardInterrupt:
            print("User interrupt")
            keep_running = False
          break
        if n > 0:
          print(" %d retries, %d Writes,  %d/%d retries(once/multiple)" %
                (n, sx0.writes - old_writes , sx0.one_retry - old_serror,
                 sx0.retries - old_merror))
        else:
          print("done")
      #Disable test hits even when not selected
      try:
        sx0.write(192,15,0)
        sx0.write(192,3,0)
        #Stop DMA
        g.regs.datapath.triv_proc.ctrl.run.writef(0)
      except Exception as e:
        continue

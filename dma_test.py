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

def portsetup(port):
    print("Testing port %d" % port)
    try:
        g.gbtfpga[port].init(attempts=20)
    except Exception as e:
        print("Fiber link %d not usable" % port)
    time.sleep(0.1)

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
    for sx0 in smxes:
        # enable channel mask, disable dummy and MSB hits
        sx0.write(192,  3, 1)
        # disable all channel
        sx0.write(192,  4, 0x3fff)
        sx0.write(192,  5, 0x3fff)
        sx0.write(192,  6, 0x3fff)
        sx0.write(192,  7, 0x3fff)
        sx0.write(192,  8, 0x3fff)
        sx0.write(192,  9, 0x3fff)
        sx0.write(192, 10, 0x3fff)
        sx0.write(192, 11, 0x3fff)
        sx0.write(192, 12, 0x3fff)
        sx0.write(192, 13, 0x3fff)
        #disable test mode
        sx0.write(192, 18, 0)
        sx0.write(192, 19, 0x300)
    #Configure generation of packet every 0.1 second
    g.regs.datapath.triv_proc.pkt_duration.write(4000000)
    #Start DMA
    g.regs.datapath.triv_proc.ctrl.reset.writef(1)
    time.sleep(0.01)
    g.regs.datapath.triv_proc.ctrl.reset.writef(0)
    time.sleep(0.01)
    g.regs.datapath.triv_proc.ctrl.run.writef(1)
    return smxes

def get_uplink(smxes, link):
    for sx0 in smxes:
        for uplink in sx0.uplinks:
            if link == uplink:
                return sx0
    print("no uplink %d" % link)

smxes = portsetup(0)
sx0 = get_uplink(smxes, 15)

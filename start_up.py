# Rewrite of xyter_control
import sys
import time
import Environment as Env
import geri
import importlib
import PFAD_lib

import logging as log
log.basicConfig(level=log.WARN, format='%(filename)s:%(lineno)d:%(levelname)s: %(message)s')

g=geri.Geri()
g.init()

# GBT (SFP) port that should be used
if len(sys.argv)  > 1:
  port = int(sys.argv[1])
else :
  port = 0

print("Trying GBT Link %d" % port)
print(g.gbtfpga[port].gbtfpga_get_link_status())
g.gbtfpga[port].init(attempts=20)

print(g.gbtfpga[port].gbtfpga_get_link_status())
#time.sleep(1)

print(g.gbtfpga[port].gbtfpga_get_link_status())

# sometimes the first operation fails...
# TODO: identify and fix the problem
time_start = time.time()
N_RETRIES = 10
for i in range(N_RETRIES):
    try:
        ver=g.gbtfpga[port].emu_regs.VER.read()
        id=g.gbtfpga[port].emu_regs.ID.read()
        if ver == 0 or id == 0:
          continue
        print(f"Read GBTxEMU firmware ID: 0x{id:08x} and VER: 0x{ver:08x}")
        break
    except Exception as e:
        if i < N_RETRIES - 1:
          pass
        else :
          print("Contacting Emu failed after %.3f seconds" % (time.time() - time_start))
          sys.exit()
    else:
        print("s.VER.read failed")
        sys.exit()
print("Contacting Emu took %.3f seconds" % (time.time() - time_start))

from hctsp import *

CH_MAX = 127

setup_elements = g.scan_setup(port)
print("Setup scan results:\n{}".format(setup_elements))

for se in setup_elements:
    se.characterize_clock_phase()
    se.initialize_clock_phase()
    se.characterize_data_phases()
    se.initialize_data_phases()
    se.scan_smx_asics_map()
for se in setup_elements:
    se.synchronize_elink()
    se.hctsp_uplink.set_uplinks_mask()
    se.write_smx_elink_masks()

import smx
smxes = []
for se in setup_elements:
    sxs = smx.smxes_from_setup_element(se)
    smxes.extend(sxs)
if smxes == []:
  print("No working uplink found")
  sys.exit()

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
  print("\nFound Group {}  Downlink {}  address {} Uplinks {} Efuse {}"
          .format(sx0.group, sx0.downlink, sx0.address, sx0.uplinks, sx0.efuse_str))

from PFAD_lib import *
def ENC_Scan(nr_smx="ALL", dump = False):
  importlib.reload(Env)
  importlib.reload(PFAD_lib)

  if not os.path.exists(Env.log_path) :
    os.mkdir(Env.log_path)
    outfilename =  Env.log_path + "/stat.txt"
    outfile = open(outfilename, "w")
  print("Using %s" % Env.log_path)
  for smx in smxes:
    if nr_smx != "ALL" and smx.efuse_str != nr_smx:
      continue
    reads = smx.reads
    writes = smx.writes
    one_retry = smx.one_retry
    retries = smx.retries
    timeouts = smx.err_timeout
    time_start = time.time()
    print("\nNow at Group {}  Downlink {}  Uplinks {} Efuse {}"
          .format(smx.group, smx.downlink, smx.uplinks, smx.efuse_str))
    if initialise(smx):
      print("Init failed")
      continue
    #set_trim(smx)
    #trim_calibration(smx)
    #if (smx.uplinks[0]==14): read_registers(smx)
    #if (smx.uplinks[0]==14): read_trim(smx)
    #if (smx.uplinks[0]==23):  check_trim(smx)
    #fast_ENC(smx)
    ENC_scurves_scan(smx, dump)
    outfile.write("GBT %d: DL %d, Addr %d, Chip %s: %d R, %d W,  %d/%d Retries(1/m), %d T_OUT\n"
                  % (port, smx.downlink, smx.address, smx.efuse_str, smx.reads -reads, smx.writes - writes,
                     smx.one_retry - one_retry, smx.retries - retries, smx.err_timeout - timeouts))
    outfile.flush()
    #channel_test(smx)
    time_end = time.time()
    print( "Duration: {:.2f}".format(time_end - time_start))

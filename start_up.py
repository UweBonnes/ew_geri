# Rewrite of xyter_control
import sys
import time
import Environment as Env
import geri
import importlib
from PFAD_lib import *

import logging as log
log.basicConfig(level=log.INFO, format='%(filename)s:%(lineno)d:%(levelname)s: %(message)s')

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

while True:
  try:
    importlib.reload(Env)
    if not os.path.exists(Env.log_path) :
      os.mkdir(Env.log_path)
      outfilename =  Env.log_path + "/stat.txt"
      outfile = open(outfilename, "w")
    for smx in smxes:
      if smx.uplinks[0] != 26:
        continue
      reads = smx.reads
      writes = smx.writes
      one_retry = smx.one_retry
      retries = smx.retries
      timeouts = smx.err_timeout
      time_start = time.time()
      print("\nNow at Group {}  Downlink {}  Uplinks {}"
            .format(smx.group, smx.downlink, smx.uplinks))
      if initialise(smx):
        print("Init Chip Group {}  Downlink {}  Uplinks {} failed"
              .format(smx.group, smx.downlink, smx.uplinks))
        continue
      #set_trim(smx)
      #trim_calibration(smx)
      #if (smx.uplinks[0]==14): read_registers(smx)
      #if (smx.uplinks[0]==14): read_trim(smx)
      #if (smx.uplinks[0]==23):  check_trim(smx)
      #fast_ENC(smx)
      ENC_scurves_scan(smx)
      outfile.write("GBT %d: DL %d, Addr %d, %d R, %d W,  %d/%d Retries(1/m), %d T_OUT\n"
                    % (port, smx.downlink, smx.address, smx.reads -reads, smx.writes - writes,
                       smx.one_retry - one_retry, smx.retries - retries, smx.err_timeout - timeouts))
      outfile.flush()
      #channel_test(smx)
      time_end = time.time()
      print( "Duration: {:.2f}".format(time_end - time_start))
      input("Press Enter to continue, ^C to exit")
  except KeyboardInterrupt:
    break

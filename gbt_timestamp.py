import sys
import time
import geri

import logging as log
log.basicConfig(format='%(filename)s:%(lineno)d - %(message)s')

g=geri.Geri()
g.init()

# GBT (SFP) port that should be used
if len(sys.argv)  > 1:
  port = int(sys.argv[1])
else :
  port = 0

print("Using port %d" % port)

#Configure generation of packet every ~0.1 second
g.regs.datapath.triv_proc.pkt_duration.write(0x400000)
#Start DMA
g.regs.datapath.triv_proc.ctrl.reset.writef(1)
time.sleep(0.001)
g.regs.datapath.triv_proc.ctrl.reset.writef(0)
time.sleep(0.001)
print("turning off all group data")
g.regs.datapath.triv_proc.ctrl.run.writef(1)
g.regs.datapath.triv_proc.ctrl.crob_disable.writef(0xff)
time.sleep(5)
print("turning on data from group 6")
g.regs.datapath.triv_proc.ctrl.crob_disable.writef(0xbf)
time.sleep(5)
print("turning on data from group 7")
g.regs.datapath.triv_proc.ctrl.crob_disable.writef(0xef)
time.sleep(5)
print("turning on data from group 6 + 7")
g.regs.datapath.triv_proc.ctrl.crob_disable.writef(0x3f)
time.sleep(5)
print("Data on GBTonly")
g.regs.datapath.triv_proc.ctrl.crob_disable.writef(0xc0)
time.sleep(5)
print("done")
g.regs.datapath.triv_proc.ctrl.run.writef(0)

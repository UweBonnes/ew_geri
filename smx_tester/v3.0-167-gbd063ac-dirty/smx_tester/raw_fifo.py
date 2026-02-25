from . import wb_read_fifo

import logging as log

class raw_frame:
  def __init__(self, data, time = None):
    self.fifodata = data
    
    if time==None:
      self.fifotime = 0
      
      self.systime = 0

    else:
      self.fifotime = time

      # bits 39..8 are stored in time fifo
      # bits 7..0 are sotred in data fifo
      self.systime = (self.fifotime << 8) | ((data>>24) & ((1<<8)-1))
      
    # bits 23..0 contains raw SMX frame
    self.smxframe = (data >> 0) & ((1<<24)-1)
    
  def __str__(self):
    s = f"{self.__class__.__name__:10s} | 0x{self.fifoframe:06x} | "

    for k,v in self.__dict__.items():
      if k!="frame":
        s += f"{k}=0x{v:0x} "

    return s
    


class raw_fifo:
  
  def __init__(self, reg_rfifo_data, reg_rfifo_time):
    self.fdata = wb_read_fifo.wb_read_fifo(reg_rfifo_data)
    self.ftime = wb_read_fifo.wb_read_fifo(reg_rfifo_time)

  def get_data_count(self):
    return int(self.fdata.get_data_count())
  
  def reset(self):
    self.fdata.reset()

  def format(self, data, time=None):

    if (time!=None) and (len(data)!= len(time)):
      log.error("format received different number of data than time samples! Can't format the data!")
      return

    ret = []
    for i in range(len(data)):
      if time!= None:
        ret.append(raw_frame(data[i], time[i]))
      else:
        ret.append(raw_frame(data[i]))

    return ret
  
  def readout_chunk(self, nrofframes, timeout_sec=5):
    data = self.fdata.readout_chunk(nrofframes, timeout_sec)
    time = self.ftime.readout_chunk(nrofframes, timeout_sec)
    return self.format(data, time)
  
  def readout(self, nrofframes, timeout_sec=5, withsystime=True):
    # when the data is continously beeing written to fifos
    # data fifo may contain less data 
    # it is possible that data acquistion times out with less then nrofframes
    # , so there is more data in time fifo
    data = self.fdata.readout(nrofframes, timeout_sec)
    if withsystime:
        nrofdata=len(data)
        time = self.ftime.readout(nrofdata, timeout_sec)
        return self.format(data, time)
    else:
        return self.format(data)

  



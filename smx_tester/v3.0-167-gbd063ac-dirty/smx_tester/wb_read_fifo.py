import time

class wb_read_fifo:
  
  def __init__(self, reg):
    self.reg = reg

  def reset(self):
    self.reg.ctrl.wr_en.writef(0)
    self.reg.ctrl.dispatch()

    # trigger register
    self.reg.ctrl.rst.writef(1)
    self.reg.ctrl.dispatch()

    self.reg.ctrl.wr_en.writef(1)
    self.reg.ctrl.dispatch()
    
  def readout_chunk(self, nrofdata, timeout_sec=5):
    self.reset()
    return self.readout(nrofdata, timeout_sec)

  def get_data_count(self):
    return self.reg.used.read().value()

  def readout(self, nrofdata, timeout_sec=5):
    delay = 0.5
    ret = []

    nrofread = 0
    
    for i in range(int(timeout_sec/delay)):
      time.sleep(delay)

      available = self.get_data_count()
      if (available + nrofread) > nrofdata:
        available = nrofdata-nrofread

      for i in range(available):
        ret.append(self.reg.data.read().value())

      nrofread += available

      if nrofread == nrofdata:
        break

    return ret
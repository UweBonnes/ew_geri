import sys, time,os, numpy as np

base_path = os.getcwd()+'/../../../'

config_and_calibration_path = base_path + 'config_and_calibration_files/'
runid = time.strftime("%y%m%d_%H%M%S", time.localtime())
log_path = base_path + 'log_files/' + runid
phases_path = config_and_calibration_path + 'clock_and_data_phases/'
DAQ_path = base_path + 'data_files/root_files/'

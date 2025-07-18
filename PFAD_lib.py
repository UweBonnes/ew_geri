
"""
PFAD_lib with minimum tools for the ASICs initialisation and diagnostics (PFAD with GERI)
M. Enciu - October 2022
"""

import smx
import sys, os, time, numpy as np, matplotlib.pyplot as plt
import progressbar
from os import path
import Environment as Env
from ROOT import TFile, TTree, TH1F, TCanvas, TGraph, TF1, TAxis

from termcolor import colored


import logging as log
log.basicConfig(level=log.INFO, format='%(filename)s:%(lineno)d - %(message)s')

CH_MIN = 0
CH_MAX_EXT = 128
CH_MAX = 127

def PFAD_configuration_list_of_ASICs():
    nul = 320
    #List of ASICs (UL    group     name    position)
    ASIC_ul = []
    ASIC_group = []
    ASIC_name = ["" for i in range(nul)]
    ASIC_position = ["" for i in range(nul)]
    outfilename = 'PFAD_configuration/list_of_ASICs/list_of_asics.txt'
    if os.path.exists(outfilename):
        with open(outfilename) as f:
            for line in f:
                x, g, y, z= line.split()    # group 
                ASIC_ul.append(int(x))
                ASIC_group.append(int(g))
                ASIC_name[(int(g))*40+int(x)] = y
                ASIC_position[(int(g))*40+int(x)] = z
    return ASIC_ul,ASIC_group,ASIC_name,ASIC_position
    
    
def initialise(smx):
    outfilename = 'PFAD_configuration/register_config/list_register_config.txt'
    ASIC_name = []
    try:
        if os.path.exists(outfilename):
            ASIC_ul,ASIC_group,ASIC_name,ASIC_position = PFAD_configuration_list_of_ASICs()
            nul = 320    # old setting, 8 downlinks with up to 40 uplinks
            #List of registers (UL    name    position)
            registers_130 = np.full((19,nul),0)
            ana_chan_63 = np.full((nul),0)	     
            ana_chan_65 = np.full((nul),0) 	     
            ana_chan_67 = np.full((nul),0) 	    
            outfilename = 'PFAD_configuration/register_config/list_register_config.txt'
            with open(outfilename) as f:
                for line in f:
                    row = line.split()
                    ul = int(row[0])
                    group = int(row[1])
                    for reg in range(0,19):
                        registers_130[reg][(group)*40+ul]=int(row[reg+2])
                        #print("{} {} {} {} {}".format(ul,group,row[21],row[22],row[23]))
                    ana_chan_63[(group)*40+ul]=int(row[21])
                    ana_chan_65[(group)*40+ul]=int(row[22])
                    ana_chan_67[(group)*40+ul]=int(row[23])

            print('Initialising at uplink {} of group {}'.format(smx.uplinks[0],smx.group))

            for ch in range(0, 128):
                smx.write(ch, 63, ana_chan_63[smx.group*40+smx.uplinks[0]])
                smx.write(ch, 65, ana_chan_65[smx.group*40+smx.uplinks[0]])
                smx.write(ch, 67, ana_chan_67[smx.group*40+smx.uplinks[0]])

                # Global DAC settings
                for i, val in enumerate(registers_130):
                    smx.write(130, i, val[smx.group*40+smx.uplinks[0]])
        else:
            # values from smxtester 547744ecaebb7d1
            reg_defaults = [31, 63, 163, 31, 0, 12, 32, 42, 48, 60, 128, 64, 30, 31, 27, 27, 88, 0, 121, 144, 244, 36]
            for ch in range(0, 128):
                smx.write(ch, 63, reg_defaults[19])
                smx.write(ch, 65, reg_defaults[20])
                smx.write(ch, 67, reg_defaults[21])
                # Global DAC settings
            for i in  range(0, 18):
                smx.write(130, i, reg_defaults[i])

        enable_TS_in_dummy = False
        enable_TS_MSB_change = False

        smx.write(192, 3, 0x1 + (enable_TS_in_dummy << 2) +
                  (enable_TS_MSB_change << 3))
        # Enable the channel mask
        for reg in range(4, 13):
            smx.write( 192, reg, 0X0) # Channel Mask each column does 10 channels
            smx.write(192, 13, 0b1100) # Channel Mask <3:0> : 129-126

        # Reset of counters, fifos, AFE
        smx.write(192, 2, 0b101010) # <1>: channel fifos, <3>: front-end channels
        # <5>: front-end ADC counter
        smx.write(192, 2, 0)       # Releasing this reset

        # Global gate to 0
        smx.write(130, 11, 0x0)  # Enabling the Channels-readout from backend
        smx.write(192, 27, 0)    # reset status
        smx.write(192, 24, 0)    # reset FIFO almost full counter
        smx.write(192, 30, 0)    # reset event-missed counter

        # Disable channels #
        if not ASIC_name:
            return
        outfilename = 'PFAD_configuration/disable_channels/{}.txt'.format(ASIC_name[smx.group*40+smx.uplinks[0]])
        if os.path.exists(outfilename ):
            list_disabled = []
            if (os.path.exists(outfilename)):
                with open(outfilename) as f:
                    for line in f:
                        row = line.split()
                        if (row[0] != "#"): 
                            list_disabled.append(int(row[0]))
                            group = [[] for iq in range(0,10)]
                            reg_value = [0 for ic in range(0,10)]

            #print(group)
            for i, ch in enumerate(list_disabled):
                Q = ch // 14
                R = ch % 14
                column = 4 + Q
                group[Q].append(R)
            for iq in range(0,10):
                value = 0
                for ir in range(len(group[iq])):
                    value = value + (1 << group[iq][ir])
                    #print(iq,"   ",ir,"   ",value)
                reg_value[iq] = value
                #print(iq,"   ",value)
                #print(group)
            for column in range (0,10):
                smx.write(192,column+4,reg_value[column])
                print("Disabled channels: ",list_disabled)
        return False
    except:
        return True
    
def set_trim(smx):
    ASIC_ul,ASIC_group,ASIC_name,ASIC_position = PFAD_configuration_list_of_ASICs()
    nul = 320        
            
    filename_trim = ("PFAD_configuration/trim_calibration_files/{}.txt".format(ASIC_name[smx.group*40+smx.uplinks[0]]))
    #Default values
    trim_values = [[128 for i2 in range(32)] for i3 in range(128)]
    for channel in range(128):
        trim_values[channel][31] = 0

            
    if (os.path.exists(filename_trim)):
        print('Setting trim values at UL {} of group {} ... \nfilename_trim: {}'.format(smx.uplinks[0],smx.group,filename_trim))
        #---Reading the trim values
        data = np.genfromtxt(filename_trim, comments='#')
        #channels = data[:,1]
        trim_values = data[:,][:,2:34]
    else:
        print("NO TRIM CALIBRATION FILE EXISTING at UL {} of group {}- use DEFAULT!".format(smx.uplinks[0],smx.group))
    #---Set the trim values
    for channel in range(128):
        #print("\nch: ",channel,end="   ")
        for discriminator in range(32):
            #print(int(trim_values[channel][discriminator]),end="   ")
            if (discriminator < 31):
                ADC_comparator = 61 - 2 * discriminator
                smx.write(channel, ADC_comparator,int(trim_values[channel][discriminator]))	#ADC comp
            else:
                #FAST comparator
                smx.write(channel, 67, int(trim_values[channel][discriminator]))
    return 0
    
def get_scurves_scan_map(smx, npulses, amplitude_set, ADC_min = 0, ADC_max = 31, ch_min = CH_MIN, ch_max = CH_MAX, SHslowFS = 0):
    count_map = [[[0 for i1 in range (len(amplitude_set))] for i2 in range(32)] for i3 in range(CH_MAX + 1)]
    bar = progressbar.ProgressBar(maxval = 100, widgets = [progressbar.Bar('=', 'SCURVES SCAN MAP [', ']'), ' ', progressbar.Percentage()])
    bar.start()

    ngroups = 4
    # Always start cal_grp 0
    ch_start = ch_min - ch_min % ngroups
    try:
        for iamp, amplitude in enumerate(amplitude_set):
            #print("Pulse amplitude:",amplitude)
            ibar = iamp / len(amplitude_set) * 100
            bar.update(ibar)
            amplitude_value = int(amplitude)
            if (amplitude_value<0): amplitude_value=0
            if (amplitude_value>255): amplitude_value=255
            smx.write(130, 4, amplitude_value)
            for group in range(ngroups):
                #---apply the shaping time and group of channels
                group_SHslowFS = ((SHslowFS & 0x3) << 2 | (group & 0x3))
                smx.write(130, 5, group_SHslowFS)
                #---Reset ADC counters
                smx.write(192, 2, 32)
                smx.write(192, 2,  0)
                #---trigger pulses (npulses)
                for itmp in range(npulses):
                    try:
                        smx.write(130, 11, 128)
                    except (AckMissed, AckNotReceived):
                        smx.err_timeout = smx.err_timeout + 1
                    try:
                        smx.write(130, 11, 0)
                    except (AckMissed, AckNotReceived):
                        smx.err_timeout = smx.err_timeout + 1
                #---reading the counters in each channel / ADC + fast comparator counter
                for channel in range(ch_start + group, ch_max + 1, ngroups):
                    if (channel >= CH_MAX_EXT):
                        break
                    for discriminator in range(ADC_min, ADC_max):
                        ADC_counter = 60 - 2 * discriminator
                        try:
                            count_map[channel][discriminator][iamp] = smx.read(channel, ADC_counter)# & 0xfff
                        except (AckMissed, AckNotReceived):
                            smx.err_timeout = smx.err_timeout + 1
                    #---FAST comparator
                    try:
                        count_map[channel][31][iamp] = smx.read(channel, 62) #& 0xfff
                    except (AckMissed, AckNotReceived):
                        smx.err_timeout = smx.err_timeout + 1
                #Channel 128/129 are in unexpected groups!
                if group == 0 and ch_max >= CH_MAX_EXT:
                    channel = CH_MAX_EXT + 1
                    for discriminator in range(ADC_min, ADC_max):
                        ADC_counter = 60 - 2 * discriminator
                        try:
                            count_map[channel][discriminator][iamp] = smx.read(channel, ADC_counter)# & 0xfff
                        except (AckMissed, AckNotReceived):
                            smx.err_timeout = smx.err_timeout + 1
                    #---FAST comparator
                    try:
                        count_map[channel][31][iamp] = smx.read(channel, 62) #& 0xfff
                    except (AckMissed, AckNotReceived):
                        smx.err_timeout = smx.err_timeout + 1
                if group == 3 and ch_max >= CH_MAX_EXT:
                    channel = CH_MAX_EXT
                    for discriminator in range(ADC_min, ADC_max):
                        ADC_counter = 60 - 2 * discriminator
                        try:
                            count_map[channel][discriminator][iamp] = smx.read(channel, ADC_counter)# & 0xfff
                        except (AckMissed, AckNotReceived):
                            smx.err_timeout = smx.err_timeout + 1
                    #---FAST comparator
                    try:
                        count_map[channel][31][iamp] = smx.read(channel, 62) #& 0xfff
                    except (AckMissed, AckNotReceived):
                        smx.err_timeout = smx.err_timeout + 1
        return (count_map, False)
    except:
        return (count_map, True)
    bar.finish()

def plot_channels_histo(y,title,file_name, ch_min, ch_max):
    c = TCanvas(title, title, 1800, 800)
    c.cd()
    h = TH1F(title, title, ch_max + 1 - ch_min, ch_min, ch_max)
    for i in range(ch_max - ch_min + 1):
        h.SetBinContent(i + 1, y[i + ch_min])
    h.SetStats(0);
    h.Draw()
    c.Print(file_name)

def fit_dataset_errfc_gaus(n,x,y0,maxy): 
    y = y0
    #errfc
    max_value = 0
    minx=x[0]
    maxx=x[len(x)-1]
    mean = (minx+maxx)/2
    width = 0
    if(y[0]<0.3*maxy):
        g = TGraph()
        f = TF1("f","[0]*(1+erf((x-[1])/[2]))",0,255)
        for i in range(n):
            if (max_value == 0 and y[i]>0.98*maxy): max_value == 1
            if (max_value == 1):
                y[i] = maxy
            g.SetPoint(i,x[i],y[i])
        #print(i,"    ",x[i],"   ",y[i])
        #print(g.GetN())
        #c = TCanvas("c","c",1800,1400)
        #g.SetMarkerStyle(20)
        #g.SetMarkerSize(5)
        #g.Draw("AP")

        f.SetParLimits(1,minx,maxx)
        f.SetParLimits(2,-100,100)
        g.Fit("f","MQ")
        #c.Print(Env.log_path + "Fast_ENC/test.png")
        amplitude = 2* f.GetParameter(0)
        mean = f.GetParameter(1)
        width = f.GetParameter(2)
        
        if (amplitude > maxy*1.5 or amplitude < maxy*1.5 or mean > maxx or mean < minx):
        #gaus
        #print("fit with gauss")
            g2 = TGraph()
            f2 = TF1("f2","gaus",0,255)
            f2.SetParLimits(1,minx,maxx)
            f2.SetParLimits(2,-100,100)
        
            for i in range(1,n):
                g2.SetPoint(i,(x[i-1]+x[i])/2,y[i]-y[i-1])
            g2.Fit("f2","MQ")
            mean = f2.GetParameter(1)
            width = f2.GetParameter(2)
    
            if (mean > maxx or mean < minx):
                mean = (minx+maxx)/2
                width = 0
    #print ("Mean erf:{}   Width erf:{}   Amplitude erf:{}    Mean gaus:{}   Width gaus:{}".format(mean,width,amplitude,mean2,width2))
    return mean, width

def channel_test(smx):
    """ gives yes/no for the triggering of each channel - first 4 discriminators
        should all trigger with a large amplitude (240)
    """
    ASIC_ul,ASIC_group,ASIC_name,ASIC_position = PFAD_configuration_list_of_ASICs()
            
            
    amplitude = 254
    #---ADC discriminators (31 ADC discriminators/channel)
    ADC_min = 0
    ADC_max = 4			# 31 ADC comparators + 1 FAST comparator
    #---channels:
    ch_min = 0
    ch_max = 128				# 128 channels from 0 to 127
    #---number of pulses
    npulses = 10
    #---slow shaper
    SHslowFS = 0

        
    amplitude_set = [amplitude]    
    count_map = get_scurves_scan_map(smx, npulses, amplitude_set, ADC_min, ADC_max, ch_min, ch_max, SHslowFS)
    
    runid = time.strftime("%y%m%d_%H%M%S", time.localtime())
    x = [i for i in range(128)]
    y = [-1 for i in range(128)]
    outfilename = Env.log_path + "PFAD_logging/Channel_test/Channel_test_logging_{}_{}.txt".format(ASIC_name[smx.group*40+smx.uplinks[0]], runid)
    outfile = open(outfilename, "w")
    for channel in range (ch_min, ch_max):
        fired = [0 for i in range(31)]
        print("ch: {:3d}".format(channel), end = "    ")
        outfile.write("ch: {:3d}    ".format(channel))
        for discriminator in range(ADC_min, ADC_max):
            if (count_map[channel][discriminator][0] > 0.9 * npulses):
                print("ok", end = "   ")
                outfile.write("ok    ")
                fired[discriminator] = 1
            else:
                print("-", end = "   ")
                outfile.write("-    ")
                fired[discriminator] = 0
        print("[{:3d}]".format(sum(fired)), end = "   ")
        outfile.write("[{:3d}]    ".format(sum(fired)))
        if (sum(fired) > 0):
            print("GOOD")
            outfile.write("GOOD\n")
        else:
            print("UNRESPONDING")
            outfile.write("UNRESPONDING\n")
        
        y[channel] = sum(fired)
    
    title = "Channel test for {}".format(ASIC_name[smx.group*40+smx.uplinks[0]])
    file_name = Env.log_path + "Channel_test/Channel_test_{}_{}.png".format(ASIC_name[smx.group*40+smx.uplinks[0]], runid)
    plot_channels_histo(y, title, file_name)
   
def ENC_scurves_scan(smx):
    """ gives a fast ENC analysis using the first 4 ADC comparators' noise
    """
    print ("ENC - SCURVES scan")
    time_start = time.time()
    amplitude_min = 0
    amplitude_max = 255
    amplitude_step = 1
    amplitude_n = 255
    #---ADC discriminators (31 ADC discriminators/channel)
    ADC_min = 0
    ADC_max = 31			# 31 ADC comparators + 1 FAST comparator
    #---channels:
    ch_min = CH_MIN
    ch_max = CH_MAX			# 130 channels from 0 to 129
    #---number of pulses
    npulses = 255
    #---slow shaper
    SHslowFS = 0
    
    MUCHmode = 0 
    normalization = 1
    scurve_path = Env.log_path + "/S-curve_analysis/"
    if (not os.path.exists(scurve_path)):
        os.mkdir(scurve_path)
    config_filename = Env.config_and_calibration_path + 'S-curve_analysis/settings.txt'
    try:
        f = open(config_filename)
    except IOError:
        print("S-curve_analysis/settings.txt not found")
    else:
        with f:
            for line in f:
                x, y = line.split()
                if (x == 'amplitude_min'): amplitude_min = int(y)
                if (x == 'amplitude_max'): amplitude_max = int(y)
                if (x == 'amplitude_step'): amplitude_step = int(y)
                if (x == 'amplitude_n'): amplitude_n = int(y)
                if (x == 'ADC_min'): ADC_min = int(y)
                if (x == 'ADC_max'): ADC_max = int(y)
                if (x == 'ch_min'): ch_min = int(y)
                if (x == 'ch_max'): ch_max = int(y)
                if (x == 'npulses'): npulses = int(y)
                if (x == 'SHslowFS'): SHslowFS = int(y)
                if (x == 'MUCHmode'): MUCHmode = int(y)
                if (x == 'normalization'): normalization = int(y)
    
    print("channels:[{} {}]".format(ch_min,ch_max))
    amplitude_set = [amplitude for amplitude in range(amplitude_min, amplitude_max,amplitude_step)]     
    count_map, res = get_scurves_scan_map(smx, npulses, amplitude_set,ADC_min, ADC_max, ch_min, ch_max,SHslowFS)
    if (res):
        print("Init Chip Group {}  Downlink {}  Uplinks {} failed"
              .format(smx.group, smx.downlink, smx.uplinks))
        return 
    #print(count_map)
    ident = "/d%d_a%d" % (smx.downlink, smx.address)
    rootfile = TFile.Open(scurve_path + ident + ".root", "recreate")
    h_scurve = [ [ TH1F("h_scurve_{}_{}".format(channel,discriminator),"h_scurve_{}_{}".format(channel,discriminator),amplitude_n,0,255) for discriminator in range(32) ] for channel in range(CH_MAX + 1) ]
    #Histrogram saving
    for channel in range (ch_min, ch_max + 1):
        for discriminator in range(ADC_min, ADC_max):
            if (discriminator==ADC_max):
                discriminator=31
            for iamp in range(len(amplitude_set)):
                h_scurve[channel][discriminator].SetBinContent(amplitude_set[iamp],count_map[channel][discriminator][iamp])
            h_scurve[channel][discriminator].Write()
            
    #ENC        
    if (normalization == 1):
        for channel in range(ch_min, ch_max + 1):
            for discriminator in range(32): 
                for i in range(len(count_map[channel][discriminator])):
                    if (count_map[channel][discriminator][i] > npulses):count_map[channel][discriminator][i] = npulses
    x = [i for i in range(CH_MAX + 1)]
    y = [-1 for i in range(CH_MAX + 1)]
    outfilename = scurve_path + ident + ".data"
    outfile = open(outfilename, "w")
    dropped = 0
    for channel in range (ch_min, ch_max + 1):
        #print("ch: {:3d}".format(channel))
        outfile.write("ch: {:3d}    ".format(channel))
        enc_ave = 0
        enc_n = 0

        for discriminator in range(ADC_min, ADC_max):
            # fit and get ENC[discriminator]; add to enc_ave and increase enc_n
            # count_map[channel][discriminator] vs amplitude_set
            count_sum = sum(count_map[channel][discriminator])
            adc, enc = (0, 0)
            #print(count_map[channel][discriminator], flush = True)
            if (count_sum > npulses):
                adc,enc = fit_dataset_errfc_gaus(len(amplitude_set), amplitude_set, count_map[channel][discriminator],npulses)
                enc = enc * 349
                if (MUCHmode == 1): enc = enc*6
                if (adc > 0.5 and adc < 250 and enc > 0.5 and discriminator<25 and discriminator>5):
                    enc_ave = enc_ave + enc
                    enc_n = enc_n + 1
                else:
                    if (adc <= 0.5 or adc >= 250 and enc <= 0.5):
                        dropped = dropped + 1
            #print("({:4.2f} {:4.2f})".format(adc, enc), flush = True)
            outfile.write("({:4.2f} {:4.2f})    ".format(adc, enc))
        if (enc_n > 0):
            enc_ave = enc_ave / enc_n
        else:
            enc_ave = -1
        outfile.write("enc: {:4.2f}\n".format(enc_ave))
        y[channel] = enc_ave
    outfile.close()
    if dropped > 0:
        print("Dropped %d pairs" % dropped)

    #human and gnuplot readable ENC data
    outfilename = scurve_path + ident +".txt"
    outfile = open(outfilename, "w")
    for channel in range (ch_min, ch_max + 1):
        outfile.write("%d, %d\n" % (channel, int(y[channel] + 0.5)))
    outfile.close()

    title = "ENC for Downlink %d Address %d" %(smx.downlink, smx.address)
    file_name = scurve_path + ident + ".png"
    ENC_LIMIT = 100000
    enc_limit = ENC_LIMIT
    if (MUCHmode == 1) :
        enc_limit = enc_limit * 6
    for ii in range (len(y)):
        if (y[ii] > ENC_LIMIT): y[ii] = enc_limit
    plot_channels_histo(y, title, file_name, ch_min, ch_max)

                                     


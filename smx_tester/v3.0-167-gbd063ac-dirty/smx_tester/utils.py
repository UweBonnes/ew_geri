import logging as log
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

import format.smx

def plot_adc_figure(smx_frames, channel,  file_="/tmp/smx_tester.png"):
    """Plot hits data on figure for given channel.

    Parameters
    smx_frames
        Dictionary containing lists of data samples.
    file_
        Path of file in which the figure should be saved.
    """
    for u in smx_frames.keys():
        adc = []
        for f in smx_frames[u]:
            if (type(f) is format.smx.hit) and (f.chan == channel):
                adc.append(f.adc)
        if len(adc) == 0:
            log.warning("No ADC data for channel {}".format(channel))
            return

        plt.plot(adc, "r")

    plt.savefig(file_)
    plt.show()


def pprint_uplink_frame(frame):
    if (frame >> 19) == 0b10001:
        type = "ACK - ACK"
        sequence_number = (frame >> 15) & 0b1111

        expected_crc = crc4_d20(frame >> 4)
        actual_crc = frame & 0b1111
        if expected_crc == actual_crc:
            crc_match = True
        else:
            crc_match = False

        print("Uplink frame {} is {}, sequence number {}, CRC match {}".format(int(frame), type, sequence_number, crc_match))
    else:
        print("Not implemented")

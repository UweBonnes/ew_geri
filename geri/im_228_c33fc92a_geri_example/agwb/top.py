"""
This file has been automatically generated
by the agwb (https://github.com/wzab/agwb).
Do not modify it by hand.
"""

from . import agwb


class i2c_master(agwb.Block):
    x__is_blackbox = True
    x__size = 32
    x__fields = {
        'reg':(0x0,32,(agwb.ControlRegister,))
    }


class spi_master(agwb.Block):
    x__is_blackbox = True
    x__size = 32
    x__fields = {
        'reg':(0x0,32,(agwb.ControlRegister,))
    }


class gbt_ic_ctrl(agwb.Block):
    x__size = 8
    x__id = 0xef581717
    x__ver = 0x489b6ec
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'ctrl':(0x2,(agwb.ControlRegister,
        {\
            'reset':agwb.BitField(0,0,False),\
            'start_write':agwb.BitField(1,1,False),\
            'start_read':agwb.BitField(2,2,False),\
            'gbtx_addr':agwb.BitField(9,3,False),\
        })),
        'tx_rega_nbtr':(0x3,(agwb.ControlRegister,
        {\
            'reg_addr':agwb.BitField(15,0,False),\
            'bytes_to_read':agwb.BitField(31,16,False),\
        })),
        'tx_data':(0x4,(agwb.ControlRegister,)),
        'status':(0x5,(agwb.StatusRegister,
        {\
            'tx_ready':agwb.BitField(0,0,False),\
            'rx_empty':agwb.BitField(1,1,False),\
            'gbtx_addr':agwb.BitField(8,2,False),\
        })),
        'rx_mptr_nbw':(0x6,(agwb.StatusRegister,
        {\
            'mem_ptr':agwb.BitField(15,0,False),\
            'words_read':agwb.BitField(31,16,False),\
        })),
        'rx_data':(0x7,(agwb.StatusRegister,)),
    }


class gbt_ec_ctrl(agwb.Block):
    x__size = 8
    x__id = 0x28f87d63
    x__ver = 0xd642fef9
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'ctrl':(0x2,(agwb.ControlRegister,
        {\
            'start_reset':agwb.BitField(0,0,False),\
            'start_connect':agwb.BitField(1,1,False),\
            'start_cmd':agwb.BitField(2,2,False),\
            'inject_crc_error':agwb.BitField(3,3,False),\
        })),
        'tx_cmd':(0x3,(agwb.ControlRegister,
        {\
            'command':agwb.BitField(7,0,False),\
            'addr':agwb.BitField(15,8,False),\
            'chan':agwb.BitField(23,16,False),\
            'trans_id':agwb.BitField(31,24,False),\
        })),
        'tx_data':(0x4,(agwb.ControlRegister,)),
        'status':(0x5,(agwb.StatusRegister,
        {\
            'received':agwb.BitField(0,0,False),\
            'len':agwb.BitField(8,1,False),\
            'error':agwb.BitField(16,9,False),\
        })),
        'status2':(0x6,(agwb.StatusRegister,
        {\
            'control':agwb.BitField(7,0,False),\
            'addr':agwb.BitField(15,8,False),\
            'chan':agwb.BitField(23,16,False),\
            'trans_id':agwb.BitField(31,24,False),\
        })),
        'rx_data':(0x7,(agwb.StatusRegister,)),
    }


class gbt_sc(agwb.Block):
    x__size = 32
    x__id = 0x14d5fefd
    x__ver = 0x9443b546
    x__fields = {
        'ic':(0x18,(gbt_ic_ctrl,)),\
        'ec':(0x10,(gbt_ec_ctrl,)),\
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
    }


class gbt_fpga_link(agwb.Block):
    x__size = 4
    x__id = 0x1d424d7a
    x__ver = 0x82b137f8
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'status':(0x2,(agwb.StatusRegister,
        {\
            'link_ready':agwb.BitField(0,0,False),\
            'rx_ready':agwb.BitField(1,1,False),\
            'rx_headerflag':agwb.BitField(2,2,False),\
            'rx_header_locked':agwb.BitField(3,3,False),\
            'tx_ready':agwb.BitField(4,4,False),\
            'tx_phaligned':agwb.BitField(5,5,False),\
            'tx_phaligned_val':agwb.BitField(6,6,False),\
            'rx_bufferbypas_error':agwb.BitField(7,7,False),\
            'tx_bufferbypas_error':agwb.BitField(8,8,False),\
            'rx_ic_inactive':agwb.BitField(9,9,False),\
        })),
        'status_with_clear':(0x3,(agwb.StatusRegister,
        {\
            'rx_error_cnt':agwb.BitField(7,0,False),\
            'rx_readyloss_cnt':agwb.BitField(15,8,False),\
            'rx_pattcheck_errcnt':agwb.BitField(31,16,False),\
        })),
    }


class gbt_fpga_common(agwb.Block):
    x__size = 4
    x__id = 0xbc250cf2
    x__ver = 0xce87cd96
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'ctrl':(0x2,(agwb.ControlRegister,
        {\
            'rst':agwb.BitField(0,0,False),\
            'rst_tx':agwb.BitField(1,1,False),\
            'rst_rx':agwb.BitField(2,2,False),\
            'tx_pol':agwb.BitField(3,3,False),\
            'rx_pol':agwb.BitField(4,4,False),\
            'loopback':agwb.BitField(7,5,False),\
            'loopback_gearbox':agwb.BitField(8,8,False),\
            'rx_scrambler_bypass':agwb.BitField(9,9,False),\
            'tx_scrambler_bypass':agwb.BitField(10,10,False),\
            'tx_encoding_sel':agwb.BitField(11,11,False),\
            'rx_encoding_sel':agwb.BitField(12,12,False),\
        })),
        'patgen':(0x3,(agwb.ControlRegister,
        {\
            'mode':agwb.BitField(1,0,False),\
            'const_dat_patt':agwb.BitField(9,2,False),\
            'const_wbdat_patt':agwb.BitField(17,10,False),\
        })),
    }


class crob1_gbt_iface(agwb.Block):
    x__size = 64
    x__id = 0x3cc15b86
    x__ver = 0x1e71735c
    x__fields = {
        'gbt_sc':(0x20,(gbt_sc,)),\
        'common':(0x1c,(gbt_fpga_common,)),\
        'link':(0x18,1,(gbt_fpga_link,)),\
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
    }


class crob3_gbt_iface(agwb.Block):
    x__size = 64
    x__id = 0x64ade247
    x__ver = 0xfb4c6fb6
    x__fields = {
        'gbt_sc':(0x20,(gbt_sc,)),\
        'link':(0x10,3,(gbt_fpga_link,)),\
        'common':(0xc,(gbt_fpga_common,)),\
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
    }


class hctsp_software_command_slot(agwb.Block):
    x__size = 8
    x__id = 0x88baef49
    x__ver = 0x5bd21c5a
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'control':(0x2,(agwb.ControlRegister,
        {\
            'chip_address':agwb.BitField(3,0,False),\
            'downlink_mask':agwb.BitField(15,4,False),\
            'group_mask':agwb.BitField(23,16,False),\
            'sequence_number':agwb.BitField(27,24,False),\
        })),
        'control_frame':(0x3,2,(agwb.ControlRegister,
        {\
            'request_type':agwb.BitField(1,0,False),\
            'request_payload':agwb.BitField(16,2,False),\
            'crc':agwb.BitField(31,17,False),\
        })),
    }


class hctsp_time_command_slot(agwb.Block):
    x__size = 8
    x__id = 0x531c39ab
    x__ver = 0xa4f0e185
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'control':(0x2,(agwb.ControlRegister,
        {\
            'chip_address':agwb.BitField(3,0,False),\
            'downlink_mask':agwb.BitField(15,4,False),\
            'group_mask':agwb.BitField(23,16,False),\
            'sequence_number':agwb.BitField(27,24,False),\
        })),
        'control_frame':(0x3,2,(agwb.ControlRegister,
        {\
            'request_type':agwb.BitField(1,0,False),\
            'request_payload':agwb.BitField(16,2,False),\
            'crc':agwb.BitField(31,17,False),\
        })),
        'timestamp':(0x5,(agwb.ControlRegister,)),
        'period':(0x6,(agwb.ControlRegister,)),
        'status':(0x7,(agwb.StatusRegister,
        {\
            'armed':agwb.BitField(0,0,False),\
            'armed_in_past':agwb.BitField(1,1,False),\
        })),
    }


class hctsp_master(agwb.Block):
    x__size = 128
    x__id = 0x4f37fce9
    x__ver = 0xef40502c
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'fetched_count':(0x2,(agwb.StatusRegister,)),
        'command_cycle_timestamp_0':(0x3,(agwb.StatusRegister,)),
        'command_cycle_timestamp_1':(0x4,(agwb.StatusRegister,)),
        'command_cycle_pause_width':(0x5,(agwb.ControlRegister,)),
        'encoding_modes':(0x6,36,(agwb.ControlRegister,)),
        'time_command_slots':(0x60,4,(hctsp_time_command_slot,)),\
        'special_time_command_slot':(0x58,(hctsp_time_command_slot,)),\
        'software_command_slot':(0x50,(hctsp_software_command_slot,)),\
    }


class hctsp_receiver(agwb.Block):
    x__size = 8
    x__id = 0x9eb288f1
    x__ver = 0x8ca4a913
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'clear_sequence_detectors':(0x2,(agwb.ControlRegister,)),
        'sequence_detectors_status':(0x3,(agwb.StatusRegister,
        {\
            'sos_detected':agwb.BitField(0,0,False),\
            'sos_stable0':agwb.BitField(1,1,False),\
            'sos_stable1':agwb.BitField(2,2,False),\
            'k28_1_detected':agwb.BitField(3,3,False),\
            'k28_1_stable1':agwb.BitField(4,4,False),\
            'eos_detected':agwb.BitField(5,5,False),\
            'eos_stable1':agwb.BitField(6,6,False),\
            'k28_5_detected':agwb.BitField(7,7,False),\
            'k28_5_stable1':agwb.BitField(8,8,False),\
        })),
        'errors':(0x4,(agwb.StatusRegister,
        {\
            'bitslip_change':agwb.BitField(0,0,False),\
            'code_8b10b':agwb.BitField(1,1,False),\
            'disparity_8b10b':agwb.BitField(2,2,False),\
            'decoding_8b10b':agwb.BitField(3,3,False),\
            'frame':agwb.BitField(4,4,False),\
            'heart_beat':agwb.BitField(5,5,False),\
        })),
        'errors_clear_mask':(0x5,(agwb.ControlRegister,
        {\
            'bitslip_change':agwb.BitField(0,0,False),\
            'code_8b10b':agwb.BitField(1,1,False),\
            'disparity_8b10b':agwb.BitField(2,2,False),\
            'decoding_8b10b':agwb.BitField(3,3,False),\
            'frame':agwb.BitField(4,4,False),\
            'heart_beat':agwb.BitField(5,5,False),\
        })),
        'errors_alarm_mask':(0x6,(agwb.ControlRegister,
        {\
            'bitslip_change':agwb.BitField(0,0,False),\
            'code_8b10b':agwb.BitField(1,1,False),\
            'disparity_8b10b':agwb.BitField(2,2,False),\
            'decoding_8b10b':agwb.BitField(3,3,False),\
            'frame':agwb.BitField(4,4,False),\
            'heart_beat':agwb.BitField(5,5,False),\
        })),
    }


class hctsp_ack_monitor(agwb.Block):
    x__size = 16
    x__id = 0x27650e93
    x__ver = 0x9e36d861
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'frame':(0x2,(agwb.StatusRegister,
        {\
            'missed':agwb.BitField(0,0,False),\
            'uplink_number':agwb.BitField(6,1,False),\
            'valid':agwb.BitField(7,7,False),\
            'frame':agwb.BitField(31,8,False),\
        })),
        'clear_detected':(0x3,2,(agwb.ControlRegister,)),
        'detected_0':(0x5,2,(agwb.StatusRegister,)),
        'detected_1':(0x7,2,(agwb.StatusRegister,)),
    }


class hctsp_uplink(agwb.Block):
    x__size = 512
    x__id = 0x6629c4cc
    x__ver = 0x2aa3c0af
    x__fields = {
        'receivers':(0x100,28,(hctsp_receiver,)),\
        'ack_monitor':(0xf0,(hctsp_ack_monitor,)),\
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'uplinks_mask_0':(0x2,(agwb.ControlRegister,)),
        'uplinks_mask_1':(0x3,(agwb.ControlRegister,)),
        'strict_mode_0':(0x4,(agwb.ControlRegister,)),
        'strict_mode_1':(0x5,(agwb.ControlRegister,)),
    }


class trivial_proc(agwb.Block):
    x__size = 4
    x__id = 0x791832e1
    x__ver = 0x4146b46e
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'ctrl':(0x2,(agwb.ControlRegister,
        {\
            'reset':agwb.BitField(0,0,False),\
            'run':agwb.BitField(1,1,False),\
        })),
        'pkt_duration':(0x3,(agwb.ControlRegister,)),
    }


class tfc(agwb.Block):
    x__size = 16
    x__id = 0x4ba5e55d
    x__ver = 0x9140283e
    x__fields = {
        'common':(0xc,(gbt_fpga_common,)),\
        'link':(0x8,(gbt_fpga_link,)),\
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'ctrl':(0x2,(agwb.ControlRegister,
        {\
            'sync_time':agwb.BitField(0,0,False),\
        })),
    }


class mmcm_controller(agwb.Block):
    x__size = 4
    x__id = 0x133e3702
    x__ver = 0xbe24a115
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'ctrl':(0x2,(agwb.ControlRegister,
        {\
            'ticks':agwb.BitField(11,0,False),\
            'incdec':agwb.BitField(12,12,False),\
            'start':agwb.BitField(13,13,False),\
            'rst':agwb.BitField(14,14,False),\
            'mmcm_reset':agwb.BitField(15,15,False),\
            'refclk_source':agwb.BitField(16,16,False),\
        })),
        'stat':(0x3,(agwb.StatusRegister,
        {\
            'ticks':agwb.BitField(11,0,False),\
            'busy':agwb.BitField(12,12,False),\
            'mmc_locked':agwb.BitField(13,13,False),\
        })),
    }


class datapath(agwb.Block):
    x__size = 8192
    x__id = 0x2b37340
    x__ver = 0xa8c1ffd2
    x__fields = {
        'hctsp_uplink_80':(0x1000,6,(hctsp_uplink,)),\
        'crob1_gbt_iface':(0xe00,6,(crob1_gbt_iface,)),\
        'hctsp_master_80':(0xd80,(hctsp_master,)),\
        'tfc':(0xd70,(tfc,)),\
        'triv_proc':(0xd6c,(trivial_proc,)),\
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
    }


class top(agwb.Block):
    x__size = 16384
    x__id = 0x1ed91fca
    x__ver = 0xf2a791ca
    x__fields = {
        'datapath':(0x2000,(datapath,)),\
        'i2c_master':(0x1fe0,(i2c_master,)),\
        'spi_master':(0x1fc0,(spi_master,)),\
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'clk_ref40_freq':(0x2,(agwb.StatusRegister,)),
        'clk_ref120_freq':(0x3,(agwb.StatusRegister,)),
        'clk_jcosc_freq':(0x4,(agwb.StatusRegister,)),
        'clk_recovered_freq':(0x5,(agwb.StatusRegister,)),
        'clk_recovered_vs_ref_freq':(0x6,(agwb.StatusRegister,)),
        'testreg':(0x7,(agwb.ControlRegister,)),
        'geritop_ctrl':(0x8,(agwb.ControlRegister,
        {\
            'i2cmaster_rst':agwb.BitField(0,0,False),\
            'spimaster_rst':agwb.BitField(1,1,False),\
            'jc_reset':agwb.BitField(2,2,False),\
            'jc_sync':agwb.BitField(3,3,False),\
            'clk_rec_oe':agwb.BitField(11,4,False),\
            'refclk_av':agwb.BitField(12,12,False),\
        })),
        'mmcm_controller':(0x1fbc,(mmcm_controller,)),\
    }


"""
This file has been automatically generated
by the agwb (https://github.com/wzab/agwb).
Do not modify it by hand.
"""

from . import agwb


class i2c_master_top(agwb.Block):
    x__is_blackbox = True
    x__size = 8
    x__fields = {
        'reg':(0x0,8,(agwb.ControlRegister,))
    }


class elinks(agwb.Block):
    x__size = 128
    x__id = 0xfe5b694f
    x__ver = 0xd5404b7b
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'clk_ctrl':(0x2,(agwb.ControlRegister,
        {\
            'output':agwb.BitField(2,0,False),\
            'freq':agwb.BitField(4,3,False),\
            'delay':agwb.BitField(13,5,False),\
        })),
        'clk_stat':(0x3,(agwb.StatusRegister,
        {\
            'delay_ready':agwb.BitField(0,0,False),\
            'pll_locked':agwb.BitField(1,1,False),\
        })),
        'din_ctrl':(0x4,33,(agwb.ControlRegister,
        {\
            'delay':agwb.BitField(4,0,False),\
            'bit_select':agwb.BitField(7,5,False),\
        })),
        'din_stat':(0x25,33,(agwb.StatusRegister,
        {\
            'delay_ready':agwb.BitField(0,0,False),\
        })),
        'downlink_mask':(0x46,(agwb.ControlRegister,)),
        'elink_clk_ena':(0x47,(agwb.ControlRegister,)),
    }


class hctsp_software_command_slot(agwb.Block):
    x__size = 8
    x__id = 0x88baef49
    x__ver = 0x2dcf9b71
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
    x__ver = 0x1b0e4bae
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
    x__size = 64
    x__id = 0x4f37fce9
    x__ver = 0x8b7323ad
    x__fields = {
        'time_command_slots':(0x20,4,(hctsp_time_command_slot,)),\
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'fetched_count':(0x2,(agwb.StatusRegister,)),
        'command_cycle_timestamp_0':(0x3,(agwb.StatusRegister,)),
        'command_cycle_timestamp_1':(0x4,(agwb.StatusRegister,)),
        'command_cycle_pause_width':(0x5,(agwb.ControlRegister,)),
        'encoding_modes':(0x6,6,(agwb.ControlRegister,)),
        'special_time_command_slot':(0x18,(hctsp_time_command_slot,)),\
        'software_command_slot':(0x10,(hctsp_software_command_slot,)),\
    }


class hctsp_receiver(agwb.Block):
    x__size = 8
    x__id = 0x9eb288f1
    x__ver = 0x8125e1b1
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
    x__ver = 0x10c0de37
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
    x__size = 1024
    x__id = 0x6629c4cc
    x__ver = 0xa994c44c
    x__fields = {
        'receivers':(0x200,33,(hctsp_receiver,)),\
        'ack_monitor':(0x1f0,(hctsp_ack_monitor,)),\
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'uplinks_mask_0':(0x2,(agwb.ControlRegister,)),
        'uplinks_mask_1':(0x3,(agwb.ControlRegister,)),
        'strict_mode_0':(0x4,(agwb.ControlRegister,)),
        'strict_mode_1':(0x5,(agwb.ControlRegister,)),
    }


class rfifo(agwb.Block):
    x__size = 8
    x__id = 0xf2d1ac2a
    x__ver = 0xe3e43970
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'ctrl':(0x2,(agwb.ControlRegister,
        {\
            'rst':agwb.BitField(0,0,False),\
            'wr_en':agwb.BitField(1,1,False),\
        })),
        'data':(0x3,(agwb.StatusRegister,)),
        'used':(0x4,(agwb.StatusRegister,)),
    }


class uraw_fifo_ctrl(agwb.Block):
    x__size = 16
    x__id = 0x2112a660
    x__ver = 0xd6395687
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'rcv_mac_l32':(0x2,(agwb.ControlRegister,)),
        'rcv_mac_m16':(0x3,(agwb.ControlRegister,)),
        'rcv_ip':(0x4,(agwb.ControlRegister,)),
        'dport':(0x5,(agwb.ControlRegister,)),
        'max_words':(0x6,(agwb.ControlRegister,)),
        'min_words':(0x7,(agwb.ControlRegister,)),
        'flush':(0x8,(agwb.ControlRegister,)),
    }


class uraw_ctrl(agwb.Block):
    x__size = 32
    x__id = 0x108b888d
    x__ver = 0x625b1007
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'uraw_uplinks':(0x2,10,(agwb.ControlRegister,)),
        'uraw_filter_pattern':(0xc,(agwb.ControlRegister,)),
        'uraw_filter_mask':(0xd,(agwb.ControlRegister,)),
        'uraw_inhibit_pattern':(0xe,(agwb.ControlRegister,)),
        'uraw_inhibit_mask':(0xf,(agwb.ControlRegister,)),
        'uraw_fifo':(0x10,(uraw_fifo_ctrl,)),\
    }


class top(agwb.Block):
    x__size = 4096
    x__id = 0x1ed91fca
    x__ver = 0xfcc17b36
    x__fields = {
        'uplink_80':(0xc00,(hctsp_uplink,)),\
        'uplink_160':(0x800,(hctsp_uplink,)),\
        'rawfifos':(0x600,33,(rfifo,)),\
        'rawfifos_time':(0x400,33,(rfifo,)),\
        'elinks':(0x380,(elinks,)),\
        'hctsp_master_80':(0x340,(hctsp_master,)),\
        'hctsp_master_160':(0x300,(hctsp_master,)),\
        'uraw_ctrl':(0x2e0,(uraw_ctrl,)),\
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'rw_test_reg':(0x2,(agwb.ControlRegister,)),
        'elink_clk_select':(0x3,(agwb.ControlRegister,)),
        'main_status':(0x4,(agwb.StatusRegister,
        {\
            'extjc_lock':agwb.BitField(0,0,False),\
            'extjc_unlock_cnt':agwb.BitField(8,1,False),\
        })),
        'main_ctrl':(0x5,(agwb.ControlRegister,
        {\
            'i2c_sfp_select':agwb.BitField(0,0,False),\
            'use_sw_jc':agwb.BitField(1,1,False),\
            'extjc_unlock_cnt_rst':agwb.BitField(2,2,False),\
            'extjc_hwrst':agwb.BitField(3,3,False),\
        })),
        'mac_ls3bytes':(0x6,(agwb.ControlRegister,)),
        'mac_ms3bytes':(0x7,(agwb.ControlRegister,)),
        'mac_status':(0x8,(agwb.StatusRegister,)),
        'j1b_ctrl':(0x9,(agwb.ControlRegister,
        {\
            'break_loop':agwb.BitField(0,0,False),\
            'reset':agwb.BitField(1,1,False),\
        })),
        'system_timestamp_0':(0xa,(agwb.StatusRegister,)),
        'system_timestamp_1':(0xb,(agwb.StatusRegister,)),
        'i2c_master':(0x2d8,(i2c_master_top,)),\
    }


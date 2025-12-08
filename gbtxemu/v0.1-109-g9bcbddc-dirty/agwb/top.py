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


class jitter_cleaner(agwb.Block):
    x__size = 16
    x__id = 0xf9f53aee
    x__ver = 0x7642cde2
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'clean_freq_meter':(0x2,(agwb.StatusRegister,)),
        'helper_freq_meter':(0x3,(agwb.StatusRegister,)),
        'current_phase':(0x4,(agwb.StatusRegister,)),
        'phase':(0x5,(agwb.ControlRegister,
        {\
            'offset':agwb.BitField(29,0,False),\
            'sign':agwb.BitField(30,30,False),\
        })),
        'pic_phase_start_thd':(0x6,(agwb.ControlRegister,)),
        'core_rst':(0x7,(agwb.ControlRegister,
        {\
            'pic':agwb.BitField(0,0,False),\
            'tuner':agwb.BitField(1,1,False),\
            'phase_meas':agwb.BitField(2,2,False),\
        })),
        'pic_ki':(0x8,(agwb.ControlRegister,)),
        'pic_kp':(0x9,(agwb.ControlRegister,)),
        'phase_average':(0xa,(agwb.ControlRegister,)),
        'phase_error':(0xb,(agwb.StatusRegister,)),
        'phlock_mon_stat':(0xc,(agwb.StatusRegister,
        {\
            'lock':agwb.BitField(0,0,False),\
            'unlock_cnt':agwb.BitField(16,1,False),\
        })),
        'phlock_mon_thd':(0xd,(agwb.ControlRegister,)),
        'phlock_mon_ctrl':(0xe,(agwb.ControlRegister,
        {\
            'unlock_cnt_rst':agwb.BitField(0,0,False),\
            'lock_rep':agwb.BitField(16,1,False),\
        })),
    }


class clock_tuning(agwb.Block):
    x__size = 32
    x__id = 0x761f5962
    x__ver = 0x5b8cec3
    x__fields = {
        'jitter_cleaner':(0x10,(jitter_cleaner,)),\
        'i2c_master':(0x8,(i2c_master_top,)),\
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'i2c_master_controler':(0x2,(agwb.ControlRegister,
        {\
            'ipbus_access_disable':agwb.BitField(0,0,False),\
            'rst':agwb.BitField(1,1,False),\
        })),
    }


class gbtfpga(agwb.Block):
    x__size = 8
    x__id = 0xc0a6296a
    x__ver = 0x2ab32d64
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'countWordsReceived':(0x2,(agwb.StatusRegister,)),
        'control':(0x3,(agwb.ControlRegister,
        {\
            'rst':agwb.BitField(0,0,False),\
            'tx_polarization_inv':agwb.BitField(1,1,False),\
            'rx_polarization_inv':agwb.BitField(2,2,False),\
            'loopBack':agwb.BitField(5,3,False),\
            'resetDataErrorSeenFlag':agwb.BitField(6,6,False),\
            'resetGbtRxReadyLostFlag':agwb.BitField(7,7,False),\
            'rxBitSlipRstOnEven':agwb.BitField(8,8,False),\
            'patternGeneratorSel':agwb.BitField(10,9,False),\
        })),
        'minLinkStablePeriod':(0x4,(agwb.ControlRegister,)),
        'status':(0x5,(agwb.StatusRegister,
        {\
            'txFrameClkPllLocked':agwb.BitField(0,0,False),\
            'mgtReady':agwb.BitField(1,1,False),\
            'rxFrameClkReady':agwb.BitField(2,2,False),\
            'gbtRxReady':agwb.BitField(3,3,False),\
            'gbtRxReadyLostFlag':agwb.BitField(4,4,False),\
            'rxDataErrorSeen':agwb.BitField(5,5,False),\
            'rxExtrDataWidebusErSeen':agwb.BitField(6,6,False),\
            'linkStable':agwb.BitField(7,7,False),\
        })),
    }


class gbt_link_checker(agwb.Block):
    x__size = 8
    x__id = 0x40e68787
    x__ver = 0x305a68cd
    x__fields = {
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'enable':(0x2,(agwb.ControlRegister,
        {\
            'en':agwb.BitField(0,0,False),\
        })),
        'config':(0x3,(agwb.ControlRegister,
        {\
            'rx_widebus_mode':agwb.BitField(0,0,False),\
            'init_value':agwb.BitField(20,1,False),\
        })),
        'status':(0x4,(agwb.StatusRegister,
        {\
            'rx_synced':agwb.BitField(0,0,False),\
        })),
        'num_of_err_frames':(0x5,(agwb.StatusRegister,)),
    }


class elinks(agwb.Block):
    x__size = 64
    x__id = 0xfe5b694f
    x__ver = 0x5c691122
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
        'din_ctrl':(0x4,28,(agwb.ControlRegister,
        {\
            'delay':agwb.BitField(4,0,False),\
            'bit_select':agwb.BitField(7,5,False),\
        })),
        'din_stat':(0x20,28,(agwb.StatusRegister,
        {\
            'delay_ready':agwb.BitField(0,0,False),\
        })),
        'downlink_mask':(0x3c,(agwb.ControlRegister,)),
        'elink_clk_ena':(0x3d,(agwb.ControlRegister,)),
    }


class top(agwb.Block):
    x__size = 128
    x__id = 0x1ed91fca
    x__ver = 0xd2a9104a
    x__fields = {
        'elinks':(0x40,(elinks,)),\
        'clock_tuning':(0x20,(clock_tuning,)),\
        'ID':(0x0,(agwb.StatusRegister,)),\
        'VER':(0x1,(agwb.StatusRegister,)),\
        'main_ctrl':(0x2,(agwb.ControlRegister,
        {\
            'gbt_ic_enable':agwb.BitField(0,0,False),\
            'i2c_sfp_select':agwb.BitField(1,1,False),\
            'use_sw_jc':agwb.BitField(2,2,False),\
            'extjc_unlock_cnt_rst':agwb.BitField(3,3,False),\
            'extjc_hwrst':agwb.BitField(4,4,False),\
        })),
        'mac_ls3bytes':(0x3,(agwb.ControlRegister,)),
        'mac_ms3bytes':(0x4,(agwb.ControlRegister,)),
        'main_status':(0x5,(agwb.StatusRegister,
        {\
            'extjc_lock':agwb.BitField(0,0,False),\
            'extjc_unlock_cnt':agwb.BitField(8,1,False),\
        })),
        'rw_test_reg':(0x6,(agwb.ControlRegister,)),
        'j1b_ctrl':(0x7,(agwb.ControlRegister,
        {\
            'break_loop':agwb.BitField(0,0,False),\
            'reset':agwb.BitField(1,1,False),\
        })),
        'i2c_master':(0x18,(i2c_master_top,)),\
        'gbtfpga':(0x10,(gbtfpga,)),\
        'gbt_link_checker':(0x8,(gbt_link_checker,)),\
    }


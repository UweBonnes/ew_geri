: /%N_HCTSP_DOWNLINKS $6 ; \ 6
: /%N_HCTSP_UPLINKS $21 ; \ 33
: /%N_ELINK_WARN $7 ; \ 7
: /%N_RAW_FIFO_L2COUNT $e ; \ 14
: /%URAW_FIFO_L2_DEPTH $a ; \ 10
: /%N_HCTSP_GROUPS $1 ; \ 1
: // $0 ;
: //_uplink_80 // $c00 + ;
: //_uplink_80#receivers //_uplink_80 $200 + swap $8 * + ;
: //_uplink_80_ack_monitor //_uplink_80 $1f0 + ;
: //_uplink_80_ack_monitor_ID //_uplink_80_ack_monitor $0 + ;
: //_uplink_80_ack_monitor_VER //_uplink_80_ack_monitor $1 + ;
$27650e93 constant //_uplink_80_ack_monitor_ID_VAL 
$10c0de37 constant //_uplink_80_ack_monitor_VER_VAL 
: //_uplink_80_ack_monitor_frame //_uplink_80_ack_monitor $2 + ;
: //_uplink_80_ack_monitor_frame.missed //_uplink_80_ack_monitor_frame $1 $0 ;
: //_uplink_80_ack_monitor_frame.uplink_number //_uplink_80_ack_monitor_frame $7e $1 ;
: //_uplink_80_ack_monitor_frame.valid //_uplink_80_ack_monitor_frame $80 $7 ;
: //_uplink_80_ack_monitor_frame.frame //_uplink_80_ack_monitor_frame $ffffff00 $8 ;
: //_uplink_80_ack_monitor#clear_detected //_uplink_80_ack_monitor + $3 + ;
: //_uplink_80_ack_monitor#detected_0 //_uplink_80_ack_monitor + $5 + ;
: //_uplink_80_ack_monitor#detected_1 //_uplink_80_ack_monitor + $7 + ;
: //_uplink_80_ID //_uplink_80 $0 + ;
: //_uplink_80_VER //_uplink_80 $1 + ;
$6629c4cc constant //_uplink_80_ID_VAL 
$a994c44c constant //_uplink_80_VER_VAL 
: //_uplink_80_uplinks_mask_0 //_uplink_80 $2 + ;
: //_uplink_80_uplinks_mask_1 //_uplink_80 $3 + ;
: //_uplink_80_strict_mode_0 //_uplink_80 $4 + ;
: //_uplink_80_strict_mode_1 //_uplink_80 $5 + ;
: //_uplink_160 // $800 + ;
: //_uplink_160#receivers //_uplink_160 $200 + swap $8 * + ;
: //_uplink_160_ack_monitor //_uplink_160 $1f0 + ;
: //_uplink_160_ack_monitor_ID //_uplink_160_ack_monitor $0 + ;
: //_uplink_160_ack_monitor_VER //_uplink_160_ack_monitor $1 + ;
$27650e93 constant //_uplink_160_ack_monitor_ID_VAL 
$10c0de37 constant //_uplink_160_ack_monitor_VER_VAL 
: //_uplink_160_ack_monitor_frame //_uplink_160_ack_monitor $2 + ;
: //_uplink_160_ack_monitor_frame.missed //_uplink_160_ack_monitor_frame $1 $0 ;
: //_uplink_160_ack_monitor_frame.uplink_number //_uplink_160_ack_monitor_frame $7e $1 ;
: //_uplink_160_ack_monitor_frame.valid //_uplink_160_ack_monitor_frame $80 $7 ;
: //_uplink_160_ack_monitor_frame.frame //_uplink_160_ack_monitor_frame $ffffff00 $8 ;
: //_uplink_160_ack_monitor#clear_detected //_uplink_160_ack_monitor + $3 + ;
: //_uplink_160_ack_monitor#detected_0 //_uplink_160_ack_monitor + $5 + ;
: //_uplink_160_ack_monitor#detected_1 //_uplink_160_ack_monitor + $7 + ;
: //_uplink_160_ID //_uplink_160 $0 + ;
: //_uplink_160_VER //_uplink_160 $1 + ;
$6629c4cc constant //_uplink_160_ID_VAL 
$a994c44c constant //_uplink_160_VER_VAL 
: //_uplink_160_uplinks_mask_0 //_uplink_160 $2 + ;
: //_uplink_160_uplinks_mask_1 //_uplink_160 $3 + ;
: //_uplink_160_strict_mode_0 //_uplink_160 $4 + ;
: //_uplink_160_strict_mode_1 //_uplink_160 $5 + ;
: //#rawfifos // $600 + swap $8 * + ;
: //#rawfifos_ID //#rawfifos $0 + ;
: //#rawfifos_VER //#rawfifos $1 + ;
$f2d1ac2a constant //#rawfifos_ID_VAL 
$e3e43970 constant //#rawfifos_VER_VAL 
: //#rawfifos_ctrl //#rawfifos $2 + ;
: //#rawfifos_ctrl.rst //#rawfifos_ctrl $1 $0 ;
: //#rawfifos_ctrl.wr_en //#rawfifos_ctrl $2 $1 ;
: //#rawfifos_data //#rawfifos $3 + ;
: //#rawfifos_used //#rawfifos $4 + ;
: //#rawfifos_time // $400 + swap $8 * + ;
: //#rawfifos_time_ID //#rawfifos_time $0 + ;
: //#rawfifos_time_VER //#rawfifos_time $1 + ;
$f2d1ac2a constant //#rawfifos_time_ID_VAL 
$e3e43970 constant //#rawfifos_time_VER_VAL 
: //#rawfifos_time_ctrl //#rawfifos_time $2 + ;
: //#rawfifos_time_ctrl.rst //#rawfifos_time_ctrl $1 $0 ;
: //#rawfifos_time_ctrl.wr_en //#rawfifos_time_ctrl $2 $1 ;
: //#rawfifos_time_data //#rawfifos_time $3 + ;
: //#rawfifos_time_used //#rawfifos_time $4 + ;
: //_elinks // $380 + ;
: //_elinks_ID //_elinks $0 + ;
: //_elinks_VER //_elinks $1 + ;
$fe5b694f constant //_elinks_ID_VAL 
$d5404b7b constant //_elinks_VER_VAL 
: //_elinks_clk_ctrl //_elinks $2 + ;
: //_elinks_clk_ctrl.output //_elinks_clk_ctrl $7 $0 ;
: //_elinks_clk_ctrl.freq //_elinks_clk_ctrl $18 $3 ;
: //_elinks_clk_ctrl.delay //_elinks_clk_ctrl $3fe0 $5 ;
: //_elinks_clk_stat //_elinks $3 + ;
: //_elinks_clk_stat.delay_ready //_elinks_clk_stat $1 $0 ;
: //_elinks_clk_stat.pll_locked //_elinks_clk_stat $2 $1 ;
: //_elinks#din_ctrl //_elinks + $4 + ;
: //_elinks#din_ctrl.delay //_elinks#din_ctrl $1f $0 ;
: //_elinks#din_ctrl.bit_select //_elinks#din_ctrl $e0 $5 ;
: //_elinks#din_stat //_elinks + $25 + ;
: //_elinks#din_stat.delay_ready //_elinks#din_stat $1 $0 ;
: //_elinks_downlink_mask //_elinks $46 + ;
: //_elinks_elink_clk_ena //_elinks $47 + ;
: //_hctsp_master_80 // $340 + ;
: //_hctsp_master_80#time_command_slots //_hctsp_master_80 $20 + swap $8 * + ;
: //_hctsp_master_80_ID //_hctsp_master_80 $0 + ;
: //_hctsp_master_80_VER //_hctsp_master_80 $1 + ;
$4f37fce9 constant //_hctsp_master_80_ID_VAL 
$8b7323ad constant //_hctsp_master_80_VER_VAL 
: //_hctsp_master_80_fetched_count //_hctsp_master_80 $2 + ;
: //_hctsp_master_80_command_cycle_timestamp_0 //_hctsp_master_80 $3 + ;
: //_hctsp_master_80_command_cycle_timestamp_1 //_hctsp_master_80 $4 + ;
: //_hctsp_master_80_command_cycle_pause_width //_hctsp_master_80 $5 + ;
: //_hctsp_master_80#encoding_modes //_hctsp_master_80 + $6 + ;
: //_hctsp_master_80_special_time_command_slot //_hctsp_master_80 $18 + ;
: //_hctsp_master_80_software_command_slot //_hctsp_master_80 $10 + ;
: //_hctsp_master_160 // $300 + ;
: //_hctsp_master_160#time_command_slots //_hctsp_master_160 $20 + swap $8 * + ;
: //_hctsp_master_160_ID //_hctsp_master_160 $0 + ;
: //_hctsp_master_160_VER //_hctsp_master_160 $1 + ;
$4f37fce9 constant //_hctsp_master_160_ID_VAL 
$8b7323ad constant //_hctsp_master_160_VER_VAL 
: //_hctsp_master_160_fetched_count //_hctsp_master_160 $2 + ;
: //_hctsp_master_160_command_cycle_timestamp_0 //_hctsp_master_160 $3 + ;
: //_hctsp_master_160_command_cycle_timestamp_1 //_hctsp_master_160 $4 + ;
: //_hctsp_master_160_command_cycle_pause_width //_hctsp_master_160 $5 + ;
: //_hctsp_master_160#encoding_modes //_hctsp_master_160 + $6 + ;
: //_hctsp_master_160_special_time_command_slot //_hctsp_master_160 $18 + ;
: //_hctsp_master_160_software_command_slot //_hctsp_master_160 $10 + ;
: //_uraw_ctrl // $2e0 + ;
: //_uraw_ctrl_ID //_uraw_ctrl $0 + ;
: //_uraw_ctrl_VER //_uraw_ctrl $1 + ;
$108b888d constant //_uraw_ctrl_ID_VAL 
$625b1007 constant //_uraw_ctrl_VER_VAL 
: //_uraw_ctrl#uraw_uplinks //_uraw_ctrl + $2 + ;
: //_uraw_ctrl_uraw_filter_pattern //_uraw_ctrl $c + ;
: //_uraw_ctrl_uraw_filter_mask //_uraw_ctrl $d + ;
: //_uraw_ctrl_uraw_inhibit_pattern //_uraw_ctrl $e + ;
: //_uraw_ctrl_uraw_inhibit_mask //_uraw_ctrl $f + ;
: //_uraw_ctrl_uraw_fifo //_uraw_ctrl $10 + ;
: //_uraw_ctrl_uraw_fifo_ID //_uraw_ctrl_uraw_fifo $0 + ;
: //_uraw_ctrl_uraw_fifo_VER //_uraw_ctrl_uraw_fifo $1 + ;
$2112a660 constant //_uraw_ctrl_uraw_fifo_ID_VAL 
$d6395687 constant //_uraw_ctrl_uraw_fifo_VER_VAL 
: //_uraw_ctrl_uraw_fifo_rcv_mac_l32 //_uraw_ctrl_uraw_fifo $2 + ;
: //_uraw_ctrl_uraw_fifo_rcv_mac_m16 //_uraw_ctrl_uraw_fifo $3 + ;
: //_uraw_ctrl_uraw_fifo_rcv_ip //_uraw_ctrl_uraw_fifo $4 + ;
: //_uraw_ctrl_uraw_fifo_dport //_uraw_ctrl_uraw_fifo $5 + ;
: //_uraw_ctrl_uraw_fifo_max_words //_uraw_ctrl_uraw_fifo $6 + ;
: //_uraw_ctrl_uraw_fifo_min_words //_uraw_ctrl_uraw_fifo $7 + ;
: //_uraw_ctrl_uraw_fifo_flush //_uraw_ctrl_uraw_fifo $8 + ;
: //_ID // $0 + ;
: //_VER // $1 + ;
$1ed91fca constant //_ID_VAL 
$fcc17b36 constant //_VER_VAL 
: //_rw_test_reg // $2 + ;
: //_elink_clk_select // $3 + ;
: //_main_status // $4 + ;
: //_main_status.extjc_lock //_main_status $1 $0 ;
: //_main_status.extjc_unlock_cnt //_main_status $1fe $1 ;
: //_main_ctrl // $5 + ;
: //_main_ctrl.i2c_sfp_select //_main_ctrl $1 $0 ;
: //_main_ctrl.use_sw_jc //_main_ctrl $2 $1 ;
: //_main_ctrl.extjc_unlock_cnt_rst //_main_ctrl $4 $2 ;
: //_main_ctrl.extjc_hwrst //_main_ctrl $8 $3 ;
: //_mac_ls3bytes // $6 + ;
: //_mac_ms3bytes // $7 + ;
: //_mac_status // $8 + ;
: //_j1b_ctrl // $9 + ;
: //_j1b_ctrl.break_loop //_j1b_ctrl $1 $0 ;
: //_j1b_ctrl.reset //_j1b_ctrl $2 $1 ;
: //_system_timestamp_0 // $a + ;
: //_system_timestamp_1 // $b + ;
: //_i2c_master // $2d8 + ;

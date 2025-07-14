ew_geri# fpga_artifacts

Files around Xyter, GBTxEmu and Geri

Should be placed as geri/soft/ew_geri and used instead of ew_strasse

When geri is under git controll, use as

[submodule "soft/ew_geri"]
        path = soft/ew_geri
        url = git@github.com:UweBonnes/ew_geri.git

Flash programming:
Initial programming needs to enable quad SPI mode. Do like
 ~/devel/openFPGALoader/build/openFPGALoader -b te0712_8 -f --enable-quad ~/devel/obertelli/ew_geri/gbtxemu/v0.1-102-g76c62b9-dirty/gbtxemu_sts6_sfp0-vivado/gbtxemu_0.bit
 or with VIVADO

Strasse vs Lintott:
Link to the righ files:
geri/soft> ln -sf ew_geri/gbtxemu/v0.1-102-g76c62b9-dirty/agwb_emu/gbtxemu_sts/ agwb_emu
or
geri/soft> ln -fs ew_geri/gbtxemu/v0.1-102-g76c62b9-dirty/agwb_emu/gbtxemu_lintott/ agwb_emu

Use correct number for N_HCTSP_UPLINKS in agwb/top_const.py
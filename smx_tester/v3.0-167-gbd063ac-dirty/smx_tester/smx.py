import time

from hctsp import *

class Smx():
    """Class implementing the SMX object in the tester."""

    def __init__(
        self,
        group,
        downlink,
        address,
        asic_uplinks,
        uplinks,
        uplinks_map,
        command_slot,
        ack_monitor,
        refclk_frq=160e6
    ):
        self.group = group
        self.downlink = downlink
        self.address = address
        self.asic_uplinks = asic_uplinks
        self.uplinks = uplinks
        self.uplinks_map = uplinks_map
        self.command_slot = command_slot
        self.ack_monitor = ack_monitor
        self.refclk_frq=refclk_frq

        self.cmd = Command(1 << self.group, 1 << self.downlink, 0, (WRADDR, WRDATA), 0, 0, self.address)

    def read(self, row, col):
        log.info("Reading SMX {}, column {}, row {}".format(hex(self.address), col, row))
        self.cmd.reevaluate(
            sequence_number=1,
            request_types=(RDDATA, NO_OP),
            register_address=(col << 8) | row
        )
        self.command_slot.issue(self.cmd)

        return self.ack_monitor.check_read()

    def write(self, row, col, data):
        log.info("Writing SMX {}, column {}, row {}, data {}".format(hex(self.address), col, row, hex(data)))
        self.cmd.reevaluate(
            sequence_number=0,
            request_types=(WRADDR, WRDATA),
            register_address=(col << 8) | row,
            data=data
        )
        self.command_slot.issue(self.cmd)

        return self.ack_monitor.check_write()

    # roughtly calculate expected data throughput based on rate and div from TEST_CTRL2 register
    def thg_calc_througput(self, rate, div):
        max_thg_rate = self.refclk_frq/3
        divider = 32/rate * (2**div)
        return max_thg_rate/divider

    # find rate and div values that will produce a throughput of expected_hit_throughput 
    def thg_find_divider_by_throughput(self, expected_hit_throughput):
        
        # make a dictionary of possible values
        throughputs = {}
        for rate in range(1, 32):
            for div_exp in range(8):
                throughputs[rate,div_exp] = self.thg_calc_througput(rate,div_exp)

        # look for the first value that is lower than expected
        for key in sorted(throughputs, key=throughputs.get ):
            tp = throughputs[key]
            
            if tp <= expected_hit_throughput:
                break

        log.info(f"Selected THG dividers: {key}, which produce {tp} hits per second. (assuming that SMX is woring with {self.refclk_frq/1e6} MHz refclock)")
        return key

    # find rate and div values that will produce a throughput which is a specified fraction of TOTAL chip throuput (all elinks)
    def thg_find_divider_by_elink_usage(self, elink_usage):
        if (elink_usage>1) or (elink_usage<0): ValueError("Must be [0,1]")

        elinks = len(self.uplinks)
        # *2 - uplinks work on DDR
        # /30 - each frame is 30 bits (after encoding)
        elink_throghput = 2*self.refclk_frq/30
        chip_throghput = elink_throghput*elinks

        return self.thg_find_divider_by_throughput(0, elink_usage*chip_throghput)

    def thg_set_throughput(self, rate, div, randbits=0):
        if rate>=2**5:      raise ValueError("Must be 5 bits.")
        if randbits>=2**3:   raise ValueError("Must be 3 bits.")
        if div>=2**3:       raise ValueError("Must be 3 bits.")

        self.write(192, 19, rate | (randbits<<5) | (div<<8) )
    
    def thg_mode_raw(self):
        self.write(192, 18, 0 )

    def thg_mode_counter(self):
        self.write(192, 18, 1 )
    
    def thg_mode_aritf_hits(self):
        self.write(192, 18, 2 )


def smxes_from_setup_element(se):
    """Create Smx objects based on setup_element.

    Returns
    -------
    List of Smx objects.
    """
    ret = []

    for asic in sorted(se.asics_map):
        smx = Smx(
            se.group,
            se.downlink,
            asic,
            se.asics_map[asic]["ASIC uplinks"],
            se.asics_map[asic]["uplinks"],
            se.asics_map[asic]["uplinks map"],
            se.hctsp_master.software_command_slot,
            se.hctsp_uplink.ack_monitor,
        )
        ret.append(smx)

    return ret

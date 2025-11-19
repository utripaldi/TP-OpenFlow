import json
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from collections import namedtuple
import os

log = core.getLogger()

class Firewall(EventMixin):
    def __init__(self):
        self.listenTo(core.openflow)
        log.debug("Enabling Firewall Module")
    
    def __init__(self):
        # Load rules
        with open("firewall_rules.json", "r") as f:
            self.config = json.load(f)

        self.selected_switches = self.config.get("selected_switches", [])
        self.rules = self.config.get("rules", [])

        # Register for OpenFlow events
        self.listenTo(core.openflow)

        log.debug("Enabling Firewall Module")

    def _handle_ConnectionUp(self, event):
        log.info("Switch connected: DPID={}".format(event.dpid))
        if event.dpid == 1:
            log.info("Firewall activated at switch s1")
            self.add_firewall_rules(event.connection)

    def add_firewall_rules(self, connection):
        self.block_port_80(connection)

        self.block_udp_traffic(connection)

        self.block_hl1_hl2_traffic(connection)

    def block_port_80(self, connection):
        msg = of.ofp_flow_mod()
        msg.match.dl_type = 0x0800
        msg.match.nw_proto = 6
        msg.match.tp_dst = 80
        connection.send(msg)

        msg = of.ofp_flow_mod()
        msg.match.dl_type = 0x0800
        msg.match.nw_proto = 17
        msg.match.tp_dst = 80
        connection.send(msg)

        log.info("Firewall: Blocked traffic to port 80")

    def block_udp_traffic(self, connection):
        msg = of.ofp_flow_mod()
        msg.match.dl_type = 0x0800
        msg.match.nw_proto = 17
        msg.match.tp_dst = 5001
        msg.match.nw_src = "10.0.0.1"
        connection.send(msg)
        log.info("Firewall: Blocked traffic UDP from port 5001 with MAC 00:00:00:00:00:01")

    def block_hl1_hl2_traffic(self, connection):
        msg = of.ofp_flow_mod()
        msg.match.dl_type = 0x0800
        msg.match.nw_src = "10.0.0.1"
        msg.match.nw_dst = "10.0.0.2"
        connection.send(msg)

        msg = of.ofp_flow_mod()
        msg.match.dl_type = 0x0800
        msg.match.nw_src = "10.0.0.2"
        msg.match.nw_dst = "10.0.0.1"
        connection.send(msg)

        log.info("Firewall: blocked communication between 10.0.0.1 and 10.0.0.2")


def launch():
    core.registerNew(Firewall)

import json
from pox.core import core
import pox.openflow.libopenflow_01 as of
from pox.lib.revent import *
from pox.lib.util import dpidToStr
from pox.lib.addresses import EthAddr
from pox.lib.addresses import IPAddr
from collections import namedtuple
import os

log = core.getLogger()
RULES_FILE = os.path.join(os.path.dirname(__file__), "firewall_rules.json")

class Firewall(EventMixin):
    def __init__(self):
        try:
            with open(RULES_FILE, "r") as f:
                self.config = json.load(f)
        except Exception as e:
            log.error("Cannot load firewall rules: {}".format(e))
            self.config = {}

        self.selected_switches = self.config.get("selected_switches", [])
        self.rules = self.config.get("rules", [])

        self.listenTo(core.openflow)
        log.debug("Firewall module initialized with rules: {}".format(self.rules))

    def _handle_ConnectionUp(self, event):
        dpid = event.dpid
        log.info("Switch connected: DPID={}".format(dpid))
        if dpid in self.selected_switches:
            log.info("Firewall activated on switch s{}".format(dpid))
            self.add_firewall_rules(event.connection)
        else:
            log.info("Switch s{} not selected for firewall".format(dpid))

    def add_firewall_rules(self, connection):
        log.info("Applying dynamic firewall rules from JSON...")

        for rule in self.rules:
            msg = of.ofp_flow_mod()

            if "dl_type" in rule:
                msg.match.dl_type = rule["dl_type"]
            if "nw_proto" in rule:
                msg.match.nw_proto = rule["nw_proto"]
            if "nw_src" in rule:
                try:
                    msg.match.nw_src = IPAddr(rule["nw_src"])
                except:
                    log.error("Invalid IP format in nw_src: {}".format(rule["nw_src"]))

            if "nw_dst" in rule:
                try:
                    msg.match.nw_dst = IPAddr(rule["nw_dst"])
                except:
                    log.error("Invalid IP format in nw_dst: {}".format(rule["nw_dst"]))
            if "tp_dst" in rule:
                msg.match.tp_dst = rule["tp_dst"]
            if "tp_src" in rule:
                msg.match.tp_src = rule["tp_src"]

            connection.send(msg)
            
            log.info("Rule applied: {}".format(rule.get("name", "Unnamed rule")))

def launch():
    core.registerNew(Firewall)

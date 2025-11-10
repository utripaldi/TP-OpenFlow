from mininet.topo import Topo

class ChainTopo(Topo):
    """
    Chain Topology en cadena:
    Two hosts at the ends and N intermediate switches connected in series.
    """

    def build(self, n=1):
        try:
            n = int(n)
        except (TypeError, ValueError):
            raise ValueError("The parameter 'n' must be an integer >= 1")

        if n < 1:
            raise ValueError("The number of switches 'n' must be >= 1")

        left_host_1 = self.addHost('hL1')
        left_host_2 = self.addHost('hL2')
        right_host_1 = self.addHost('hR1')
        right_host_2 = self.addHost('hR2')

        switches = []
        for i in range(n):
            switch = self.addSwitch(f's{i+1}')
            switches.append(switch)

        self.addLink(left_host_1, switches[0])
        self.addLink(left_host_2, switches[0])

        for i in range(n - 1):
            self.addLink(switches[i], switches[i+1])

        self.addLink(switches[-1], right_host_1)
        self.addLink(switches[-1], right_host_2)

topos = {'chain': ChainTopo}

from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.log import setLogLevel
from topologia import ChainTopo

def run():
    setLogLevel('info')
    
    topo = ChainTopo(n=3)
    
    controller = RemoteController('c0', ip='127.0.0.1', port=6633)
    
    net = Mininet(topo=topo, controller=controller)
    net.start()
    
    print("Running Mininet. Performing ping test: ")
    net.pingAll()
    
    from mininet.cli import CLI
    CLI(net)
    
    net.stop()

if __name__ == '__main__':
    run()

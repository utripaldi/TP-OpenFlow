import argparse
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.log import setLogLevel
from topologia import ChainTopo

def run(n):
    setLogLevel('info')
    
    topo = ChainTopo(n=n)
    
    controller = RemoteController('c0', ip='127.0.0.1', port=6633)
    
    net = Mininet(topo=topo, controller=controller)
    net.start()
    
    print("Running Mininet. Performing ping test: ")
    net.pingAll()
    
    from mininet.cli import CLI
    CLI(net)
    
    net.stop()

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start Mininet with Chain Topology')
    parser.add_argument('-n', '--n', type=int, default=3,
                        help='Quantity of intermediate switches (default: 3)')
    
    args = parser.parse_args()
    try:
        run(args.n)
    except Exception as e:
        print(f"Error: {e}")
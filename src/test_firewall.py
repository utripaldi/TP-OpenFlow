import argparse
from topologia import ChainTopo
from mininet.net import Mininet
from mininet.node import RemoteController
from mininet.log import setLogLevel
from mininet.cli import CLI

def run_test(description, host_src, host_dst, port, udp=False):
    proto_flag = "-u" if udp else ""
    print(f"\n[TEST] {description}")
    print(f"  -> {host_src.name} → {host_dst.name}, port={port}, udp={udp}")
    print(host_src.cmd(f'timeout -s KILL 5s iperf -c {host_dst.IP()} -p {port} {proto_flag} -t 4'))


def run(n):
    setLogLevel('info')
    
    topo = ChainTopo(n=n)
    controller = RemoteController('c0', ip='127.0.0.1', port=6633)
    net = Mininet(topo=topo, controller=controller)
    net.start()

    print("Verifying connection for all hosts with ping:")
    net.pingAll()

    hL1 = net.get('hL1')
    hL2 = net.get('hL2')
    hR1 = net.get('hR1')
    hR2 = net.get('hR2')

    run_test(
        "Any Traffic with destination port 80 must be blocked (hL1 → hR1)",
        hL1, hR1, 80, False
    )

    run_test(
        "UDP Traffic with destination port 5001 from hL1 must be blocked (hL1 → hR2)",
        hL1, hR2, 5001, True
    )

    print("\n[TEST] hL1 y hL2 must not communicate")
    print(hL1.cmd(f"ping -c 4 {hL2.IP()}"))

    run_test(
        "TCP Traffic with destination port 22 must not be blocked (hL1 → hR1)",
        hL1, hR1, 22, False
    )

    CLI(net)
    net.stop()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Start Mininet with Chain Topology')
    parser.add_argument('-n', '--n', type=int, default=3,
                        help='Quantity of intermediate switches (default: 3)')
    
    setLogLevel('info')
    args = parser.parse_args()

    try:
        run(args.n)
    except Exception as e:
        print(f"Error: {e}")

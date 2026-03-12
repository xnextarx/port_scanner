import scanner.core as core
import argparse
import threading

parser = argparse.ArgumentParser(description='port-scanning tool')
parser.add_argument('-a', '--address', required=True, type=str, help='IP address')
parser.add_argument('-p', '--port', type=int, help='Port')
parser.add_argument('-i', '--interval', type=int, help='Port interval')
args = parser.parse_args()

def main():

    if args.port is None:
        #full scan
        for i in range(1, 65535):
            addr: tuple = (args.address, i)
            thread = threading.Thread(target=core.scan_port, args=(addr,))
            thread.start()
    

    '''addr: tuple = (args.address, args.port)

    core.scan_port(addr)'''

if __name__ == "__main__":
    main()
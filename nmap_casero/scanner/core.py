import socket


def scan_port(addr):

    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    client.settimeout(1)
    
    try:
        client.connect(addr)

    except TimeoutError:
        pass

    except ConnectionRefusedError:
        pass

    else:
        print(f"{addr[0]} has the port {addr[1]} active")

    finally:
        client.close()


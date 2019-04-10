import socket, argparse
from datetime import datetime

Max_bytes = 65535

def server(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(("localhost", port))
    print("Listening at {}".format(sock.getsockname))
    while True:
        data, address = sock.recvfrom(Max_bytes)
        text = data.decode("ascii")
        print("The client at {} says {!r}".format(address, text))
        text = "Your data was {} bytes long".format(len(data))
        data = text.encode("ascii")
        sock.sendto(data, address)

def client(port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    text = "The time is {}".format(datetime.now())
    data = text.encode("ascii")
    print("The OS assigned me the address {}".format(sock.getsockname()))
    data, address = sock.recvfrom(Max_bytes)






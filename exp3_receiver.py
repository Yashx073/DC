import socket
import struct

MCAST_GRP = "224.1.1.1"
MCAST_PORT = 5007

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, socket.IPPROTO_UDP)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("", MCAST_PORT))

mreq = struct.pack("4sl", socket.inet_aton(MCAST_GRP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)

print("Receiver started... Waiting for messages")

while True:
    data, addr = sock.recvfrom(1024)
    print("Received message:", data.decode())

# Pip command for this file:
# python -m pip install --upgrade pip
# Note: This script uses only Python standard-library modules.

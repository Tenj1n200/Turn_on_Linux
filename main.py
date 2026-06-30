import socket

mac = "xx:xx:xx:xx:xx:xx"

mac = mac.replace(":", "")
packet = bytes.fromhex("FF" * 6 + mac * 16)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)
sock.sendto(packet, ("255.255.255.255", 9))

print("Magic Packet enviado!")
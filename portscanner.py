#  Port Scanner on localhost using socket lib

import sys, socket

for port in range(0,1000):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex( ("192.168.0.1", port) )
    if result == 0:
        print "Port " + str(port) + " Open."
    sock.close()

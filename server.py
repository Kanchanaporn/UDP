import socket
import math


UDP_IP = "127.0.0.1"
UDP_PORT = 5006
sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))


while True:
    data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
    data = math.factorial(int(data))
    print "Factorial of data : ", data
    #sock.sendto(str(data,UDP_IP))
    #sent = sock.send(str(data))
    

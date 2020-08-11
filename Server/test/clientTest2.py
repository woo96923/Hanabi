import socket
import threading
import sys
import time

def Recev(s):
    while True:
        data = s.recv(1024)
        print('Recevied form Server : ',data.decode())



port = 6666
size = 1024
s = None
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    s.connect(('127.0.0.1', port))
    print('connected with Server')
    r = threading.Thread(target=Recev, args=(s,))
    r.start()

except socket.error:
    if s:
        s.close()
    print("Could not open socket: ")
    sys.exit(1)

while True:
        data = input('> ')
        s.sendall(data.encode())


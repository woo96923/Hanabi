import socket
import threading
import sys
import time

"""
def ReceveOreder(size):
    #global isMyTurn

    print('thread is maked')
    while True:

        data = s.recv(size)
        print('Recevied form Server : ',data.encode())

        if data.encode == 'T1':
            m = threading.Thread(target=MyTurn())
            m.start()
            isMyTurn = 1
            """

port = 6666
size = 1024
s = None
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    s.connect(('127.0.0.1', port))
    print('connected with Server')
    # r = threading.Thread(target=ReceveOreder(size))
    # r.start()

except socket.error:
    if s:
        s.close()
    print("Could not open socket: ")
    sys.exit(1)

while True:
    print('waiting from Server')
    data = s.recv(size)
    print('Recevied form Server : ', data.decode())
    """
    data = input('> ')
    s.sendall(data.encode())
    data = s.recv(size)
    print ('Server sent:' ,data)
    """
s.close()
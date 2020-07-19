import socket
import threading
import sys

isMyTurn = 0

def ReceveOreder():


def MyTurn():

    while isMyTurn:
        data = input()
        s.sendall(data.encode())

    s.sendall('players turn end'.encode())##여기에다가 플레이어 이름이랑 방송 명령어 추가 예정



port = 6666
size = 1024
s = None
try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    s.connect(('127.0.0.1', port))
    threading.Thread.MyTurn()
except socket.error:
    if s:
        s.close()
    print ("Could not open socket: ")
    sys.exit(1)

while True:

    threading.Thread.MyTurn()
    data = input('> ')
    s.sendall(data.encode())
    data = s.recv(size)
    print ('Server sent:' ,data)
s.close()
import socket
import threading
import sys
import time

class Client():

    port = 6666
    size = 1024
    s = None

    def __init__(self, IP, port):
        self.IP = IP
        self.port = port
        self.size = 1024
        self.s = None
        # self.playerNumber = playerNumber

    def connectWithServer(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = socket.gethostname()
            self.s.connect((self.IP, self.port))
            print('connected with Server')
            self.recevePN = self.s.recv(self.size)
            self.playerNumber = self.recevePN.decode()[4]
            print('Your player number is ', self.playerNumber)
            # r = threading.Thread(target=ReceveOreder(size))
            # r.start()

        except socket.error:
            if self.s:
                self.s.close()
            print("Could not open socket: ")
            sys.exit(1)

    def Recev(s):
        while True:
            data = s.recv(1024)
            print('Recevied form Server : ',data.decode())


if __name__ == '__main__':
    while True:
        data = input('> ')
        s.sendall(data.encode())


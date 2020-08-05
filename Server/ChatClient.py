import socket
import threading
import sys
import types
import time

class client():
    def __init__(self,IP,port):
        self.IP = IP
        self.port = port
        self.size = 1024
        self.s = None
        #self.playerNumber = playerNumber



    def connectWithServer(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            host = socket.gethostname()
            self.s.connect((self.IP, self.port))
            print('connected with Server')
            self.recevePN = self.s.recv(self.size)
            self.playerNumber = self.recevePN.decode()[4]
            print('Your player number is ', self.playerNumber)


        except socket.error:
            if self.s:
                self.s.close()
            print("Could not open socket: ")
            sys.exit(1)

    def sendingMsg(self):
        while True:
            data = input()
            self.s.send(data.encode())
            self.s.close()

    def gettingMsg(self):
        while True:
            data = self.s.recv(1024)
            print(data.decode())
            self.s.close()




    def run(self):
        threading._start_new_thread(self.sendingMsg, ())
        threading._start_new_thread(self.gettingMsg, ())


c = client('localhost', 7777)
c.connectWithServer()
while True:
    c.run()

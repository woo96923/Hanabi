import socket
import threading
import sys
import types
import time

class Client():
    def __init__(self,IP,port):
        self.IP = IP
        self.port = port
        self.size = 1024
        self.s = None



    def connectWithServer(self):
        try:
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.IP, self.port))
            print('connected with Server')

            # 플레이어 넘버랑 시드 받음
            self.recevePN = self.s.recv(self.size)
            assert self.recevePN.decode()[0:4] == '//PN', "invalid PN format"
            self.playerNumber = self.recevePN.decode()[4]
            print('Your player number is ', self.playerNumber)

            self.receveSEED = self.s.recv(self.size)
            assert self.receveSEED.decode()[0:4] == '//SE', "invalid PN format"
            self.SEED = self.receveSEED.decode()[4:]
            print('Your seed is ', self.SEED)

        except socket.error:
            if self.s:
                self.s.close()
            print("Could not open socket: ")
            sys.exit(1)

    def run(self):
        '''

        :return: 내 턴일 때 명령을 전달하는 2개 또는 3개의 숫자 또는 문자 ex) 13, 351, 3G2
        '''
        while True:

            data = self.s.recv(self.size)
            return data.decode()

    def sendAction(self,Action):
        self.s.sendall(Action.encode())

    def receveAction(self):
        Action = self.s.recv(self.size)
        return Action.decode()

    def getSEED(self):
        return self.SEED

if __name__ == '__main__':
    c = Client('localhost', 6666)
    c.connectWithServer()
    # while True:
    #     c.run()
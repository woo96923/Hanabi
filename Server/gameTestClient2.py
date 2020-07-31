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
            # r = threading.Thread(target=ReceveOreder(size))
            # r.start()

        except socket.error:
            if self.s:
                self.s.close()
            print("Could not open socket: ")
            sys.exit(1)

    def run(self):
        '''

        :return: 2개 또는 3개의 숫자 또는 문자
        '''
        #print('waiting from Server')
        data = self.s.recv(self.size)
        print('Recevied form Server : ', data.decode())
        if data.decode()[0:6] == '//turn':#내 차례가 왔을 때만 답변 가능 한번만..
            if data.decode()[6] == str(self.playerNumber): #내 차례라면~
                data = input('> ')
                self.s.sendall(data.encode())

            else :#내차례까 아니면~
                print("player number ", self.playerNumber, "is playing Turn...")

            data = self.s.recv(self.size)
            assert data.decode()[0:2] == '//', "invalid commend format"
            print(data.decode())
            return data.decode()[2:]


c = client('localhost', 6666)
c.connectWithServer()
while True:
    c.run()

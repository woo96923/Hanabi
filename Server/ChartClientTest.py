import socket
import threading
import sys
import types
import time
import Server.Commends

COMMENDKEY = '//'
ITISCHAT = '#C'
ITISPLAYERNUMBER = '#P'


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
            recevePN = self.s.recv(self.size)
            if recevePN.decode()[0:2] == ITISPLAYERNUMBER:
                self.playerNumber = recevePN.decode()[2]
                print('Your player number is ', self.playerNumber)
            else:
                print('Errer in receiving PN')


        except socket.error:
            if self.s:
                self.s.close()
            print("Could not open socket: ")
            sys.exit(1)

    def sendingMsg(self,s):

        print("opend sendingMsg Thread")
        while True:
            data = input('>>>')
            s.send(data.encode())
        print("Closed sendingMsg Thread")
        s.close()

    def gettingMsg(self,s):

        print("opend gettingMsg Thread")
        while True:
            data = s.recv(1024)
            if data.decode()[0:2] == COMMENDKEY:#서버로 부터 받은게 커맨드라면
                return data
            elif data.decode()[0:2] == ITISCHAT:#채팅이라면
                print('\n','Player ',data.decode[2],' : ',data.decode()[3:])
                return ITISCHAT
        print("Closed gettingMsg Thread")
        s.close()

    def myPlayerNumberis(self):
        return self.playerNumber


    def run(self):

        get = threading.Thread(target=self.gettingMsg, args=(self.s,))
        #get.daemon = True
        get.start()

        send = threading.Thread(target=self.sendingMsg, args=(self.s,))
        #send.daemon = True
        send.start()

        #threading._start_new_thread(self.sendingMsg, ())
        #threading._start_new_thread(self.gettingMsg, ())
        #print("program is ended")


c = client('localhost', 7777)
c.connectWithServer()
c.run()
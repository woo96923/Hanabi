#!/usr/bin/env python
import socket
import sys
import threading




class Client(threading.Thread):
    def __init__(self, ip, port, connection):
        threading.Thread.__init__(self)
        self.connection = connection
        self.ip = ip
        self.port = port

        #self.send_to_all_clients('player ', port,' is connected.')##추후에 ip나 player이름으로 교체 예정

    def getMsg(self):
        data = self.connection.recv(1024)
        return data





"""
    def run(self):
        while True:
            data = self.connection.recv(1024)
            if data :

                self.connection.sendall(data)
            else :
                break
        self.connection.close()
        """


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.server = None
        self.clients = []

    def send_to_all_clients(self, msg):
        for client in self.clients :
            print('sanding message to ',client.port)
            client.connection.send(msg.encode())

    def broadCast(self):
        data = input('> ')
        print(data[:6])##내가 뭘 보냈는지 확인용
        self.send_to_all_clients(data)
        if data[:6] == '//Turn':
            temp = threading.Thread(target=self.requestMsgToClient,args=(self.clients[0].ip,self.clients[0].port))
            temp.start()
            input('waiting...')
            #self.requestMsgToClient(self.clients[0].ip,self.clients[0].port)
            #일단 //turn오면 무조건 첫번째 접속자 한테 메세지 받기
            #스레드 안쓰니까 밀려서 스레드 사용해봄



    def send_to_client(self, ip, port, msg):
        for client in self.clients :
            if client.ip == ip and client.port == port :
                client.connection.send(msg.encode())

    def requestMsgToClient(self, ip, port):
        for client in self.clients :
            if client.ip == ip and client.port == port :
                client.connection.send('//turn'.encode())
                msg = client.getMsg()
                print (msg)
                self.send_to_all_clients(msg.decode())

    def open_socket(self):
        try:
            self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server.bind(self.address)
        except socket.error as e:
            if self.server:
                self.server.close()
            sys.exit(1)

    def run(self):
        self.open_socket()
        self.server.listen(5)
        #b = threading.Thread(target= self.broadCast())
        #b.start()

        while len(self.clients)!=2 :
            connection, (ip, port) = self.server.accept()

            c = Client(ip, port, connection)
            c.start()

            self.clients.append(c)
            print(self.clients)

        print('what?')
        while True:

            self.broadCast()

            #if len(self.clients) == 4:
             #   self.send_to_all_clients('The game will begain')

        self.server.close()

if __name__ == '__main__':
    s = Server('127.0.0.1', 6666)
    s.run()
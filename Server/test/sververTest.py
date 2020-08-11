#!/usr/bin/env python
import socket
import sys
import threading
import time

clients = []


class Client(threading.Thread):
    global clients
    def __init__(self, ip, port, connection):
        threading.Thread.__init__(self)
        self.connection = connection
        self.ip = ip
        self.port = port

        #self.send_to_all_clients('player ', port,' is connected.')##추후에 ip나 player이름으로 교체 예정

    def receive(self):
        while True:

            print("Waiting msg from the client...")
            data = self.connection.recv(1024)
            self.send_to_all_clients(data)

    def send_to_all_clients(self, msg):
        for client in clients :
            print('sanding message to ', client.port)
            client.connection.send(msg)

    def run(self):
        receiver = threading.Thread(target=self.receive)
        receiver.start()



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
    global clients

    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.server = None



    def broadCast(self):
        data = input('> ')
        print(data[:6])##내가 뭘 보냈는지 확인용
        self.send_to_all_clients(data)
        if data[:6] == '//turn':
            clientNumber = int(data[6]) - 1
            self.requestMsgToClient(clients[clientNumber].ip,clients[clientNumber].port)
            #temp = threading.Thread(target=self.requestMsgToClient,args=(self.clients[clientNumber].ip,self.clients[clientNumber].port))
            #temp.start()
            #input('waiting...')
            #self.requestMsgToClient(self.clients[0].ip,self.clients[0].port)
            #일단 //turn오면 무조건 첫번째 접속자 한테 메세지 받기
            #스레드 안쓰니까 밀려서 스레드 사용해봄

    def send_to_all_clients(self, msg):#제에에발 문자열 그대로 넣으세요 아님 바꾸던가
        for client in clients :
            print('sanding message to ',client.port)
            client.connection.send(msg.encode())

    def send_to_client(self, ip, port, msg):
        for client in clients :
            if client.ip == ip and client.port == port :
                client.connection.send(msg.encode())

    def requestMsgToClient(self, ip, port):
        print("Running requestMsgToClient...")
        for client in clients :
            if client.ip == ip and client.port == port :
                print('Found selected client...',ip,port)
                #client.connection.send('//turn'.encode())
                while True:
                    msg = client.getMsg()
                    print(msg.decode())
                    if msg.decode() == '//end':
                        break
                    self.send_to_all_clients(msg.decode())
                self.send_to_all_clients('players Turn is ended')

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

        while len(clients)!=1 :
            connection, (ip, port) = self.server.accept()

            c = Client(ip, port, connection)
            c.start()

            clients.append(c)
            print(clients)

        print('All clients are connected!')
        while True:
            time.sleep(0.5)
            #self.broadCast()

            #if len(self.clients) == 4:
             #   self.send_to_all_clients('The game will begain')

        self.server.close()

if __name__ == '__main__':
    s = Server('127.0.0.1', 6666)
    s.run()
#!/usr/bin/env python
import socket
import sys
import threading

GAMESTART = 1
GAMEEND = 0
GAME = 0

playerNumber = 1

class Client(threading.Thread):

    def __init__(self, ip, port, connection):
        global playerNumber
        threading.Thread.__init__(self)
        self.connection = connection
        self.ip = ip
        self.port = port
        self.connection.sendall(('//PN'+str(playerNumber)).encode())
        playerNumber += 1

    def getMsg(self):
        print("Waiting msg from the client...")
        data = self.connection.recv(1024)
        return data


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.server = None
        self.clients = []

    def broadCast(self):
        global GAME, GAMESTART, GAMEEND

        GAME = GAMESTART
        print('Game start : //auto\nSelect player : //turn + playernumber')
        data = input('> ')
        if data == "//auto":#menu 1
            while GAME == GAMESTART:
                for number,client in enumerate(self.clients):
                    self.send_to_all_clients('//turn'+str(number+1))
                    self.requestMsgToClient(self.clients[number].ip, self.clients[number].port)
                    if GAME == GAMEEND:
                        break

        elif data[:6] == '//turn':
            self.send_to_all_clients(data)
            clientNumber = int(data[6]) - 1
            self.requestMsgToClient(self.clients[clientNumber].ip,self.clients[clientNumber].port)

    def send_to_all_clients(self, msg):#제에에발 문자열 그대로 넣으세요 아님 바꾸던가
        for client in self.clients :
            print('sanding message to ',client.port,msg)
            client.connection.send(msg.encode())

    def send_to_client(self, ip, port, msg):
        for client in self.clients :
            if client.ip == ip and client.port == port :
                client.connection.send(msg.encode())

    def requestMsgToClient(self, ip, port):#특정 client에게 메세지 하나 받아오고 //end를 받을 때 까지 반복
        global GAME,GAMESTART, GAMEEND
        print("Running requestMsgToClient...")
        for client in self.clients :
            if client.ip == ip and client.port == port :
                print('Found selected client...', ip, port)

                msg = client.getMsg()
                print(msg.decode())
                '''
                if msg.decode() == '//endgame':
                    GAME = GAMEEND
                    break
                elif msg.decode() == '//endturn':
                    break
                '''
                self.send_to_all_clients(msg.decode())
        #self.send_to_all_clients('players Turn is ended')

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

        print('All clients are connected!')

        while True:

            self.broadCast()

        self.server.close()

if __name__ == '__main__':
    s = Server('', 6666)
    s.run()
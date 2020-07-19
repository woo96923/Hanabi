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

        self.send_to_all_clients('player ', port,' is connected.')##추후에 ip나 player이름으로 교체 예정

    def run(self):
        while True:
            data = self.connection.recv(1024)
            if data :
                self.connection.sendall(data)
            else :
                break
        self.connection.close()


class Server:
    def __init__(self, ip, port):
        self.ip = ip
        self.port = port
        self.address = (self.ip, self.port)
        self.server = None
        self.clients = []

    def send_to_all_clients(self, msg):
        for client in self.clients :
            client.connection.send(msg.encode())

    def send_to_client(self, ip, port, msg):
        for client in self.clients :
            if client.ip == ip and client.port == port :
                client.connection.send(msg.encode())

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

        while True :
            connection, (ip, port) = self.server.accept()

            c = Client(ip, port, connection)
            c.start()

            self.clients.append(c)

            #if len(self.clients) == 4:
             #   self.send_to_all_clients('The game will begain')

        self.server.close()

if __name__ == '__main__':
    s = Server('127.0.0.1', 6666)
    s.run()
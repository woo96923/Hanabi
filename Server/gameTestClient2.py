import socket
import threading
import sys
import time

port = 6666
size = 1024
s = None
playerNumber = -1

try:
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = socket.gethostname()
    s.connect(('127.0.0.1', port))
    print('connected with Server')
    recevePN = s.recv(size)
    playerNumber = recevePN.decode()[4]
    print('Your player number is ',playerNumber)
    # r = threading.Thread(target=ReceveOreder(size))
    # r.start()

except socket.error:
    if s:
        s.close()
    print("Could not open socket: ")
    sys.exit(1)

while True:
    print('waiting from Server')
    data = s.recv(size)
    print('Recevied form Server : ', data.decode())
    if data.decode()[0:6] == '//turn':#내 차례가 왔을 때만 답변 가능 한번만..
        if data.decode()[6] == str(playerNumber):  # 내 차례라면~
            while data[0:5] != '//end':#이 반복문만 빼면 한번만 전송함
                data = input('> ')
                s.sendall(data.encode())
        else :#내차례까 아니면~
            print("player number ",data.decode()[6],"is playing Turn...")
        #data = s.recv(size)
        #print('Server sent Answer: ', data.decode())
    """
    data = input('> ')
    s.sendall(data.encode())
    data = s.recv(size)
    print ('Server sent:' ,data)
    """

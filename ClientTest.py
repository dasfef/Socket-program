import socket


HOST = '192.168.0.174'
PORT = 9999
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))                                                 # 서버에 원격접속

while True :
    data = client_socket.recv(1024)                                                 # 최대 1024 바이트를 1분마다 수신
    print(len(data), '바이트 수신')
    for x in data :                                                                 # 바이트배열의 크기만큼 반복
        print(x, end='')
    print('\n')
    





client_socket.close()                                                               # 접속종료
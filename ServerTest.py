import socket
from _thread import *
import pymysql
import time

def functhread(client_socket, addr) :                                                       # 클라이언트소킷을 위한 스레드
    print(addr[0], addr[1])                                                                 # 클라이언트 접속정보 출력
    
    while True :
        query = 'select * from tbldata order by s_measuretime desc limit 1'
        cursor.execute(query)                                                               # 쿼리 실행
        result = cursor.fetchall()                                                          # 1개의 레코드 반환
        data = []
        for item in result :                                                                # item은 1개의 행
            for j in range(1, 7) :
                data.append(int(item[j]))
        print(data)
        bytedata = bytearray(data)                                                          # 바이트 배열로 변환
        client_socket.sendall(bytedata)                                                     # 바이트 배열 송신
        time.sleep(60)
    
    
    print('연결종료')
    client_socket.close()                                                                   # 연결 종료




HOST = '192.168.0.174'
PORT = 9999                                                                                 # 0 ~ 65535 중에서 사용가능(0 ~ 1024는 사용 권장하지 않음)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)                           # 소킷 객체 생성
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((HOST, PORT))                                                            # 문자열과 정수
server_socket.listen()                                                                      # 클라이언트로부터 수신 준비, 서버 시작

conn = pymysql.connect(host='127.0.0.1' , user='root', password='bigdatar', db='work', charset='utf8')
        
cursor = conn.cursor()



while True :
    print('wait...')
    client_socket, addr = server_socket.accept()                                            # 대기상태, 아래 라인으로 내려가지 않음, 접속할 경우 실행되며 클라이언트소킷과 IP 를 반환
    print('접속됨')
    start_new_thread(functhread, (client_socket, addr))                                     # 스레드 생성, 동시에 여러개 스레드 생성 가능
    
    
    
    
    

server_socket.close()                                                                       # 서버 종료

import socket
import time

TCP_IP = "192.168.100.1"
TCP_PORT = 8000
BUF_SIZE = 1024

try: 
  while True:
    sockRX = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    sockRX.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sockRX.bind((TCP_IP,TCP_PORT))
    sockRX.listen(1)

    print("RX ready")

    sockConect, addr = sockRX.accept()

    lowerCase = sockConect.recv(BUF_SIZE)
    sockConect.send(lowerCase.upper())
    sockRX.close()
    time.sleep(1)

except KeyboardInterrupt:
  sockRX.close()

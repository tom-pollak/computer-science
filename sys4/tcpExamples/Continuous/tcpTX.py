import socket
import time

TCP_IP = "192.168.101.1"
TCP_PORT = 8000
BUF_SIZE = 1024

sockTX = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockTX.connect((TCP_IP, TCP_PORT))

try: 
  while True:
    lowerCase = "hello world".encode("ascii")
    sockTX.send(lowerCase)
    upperCase = sockTX.recv(BUF_SIZE).decode("ascii")
    print("TX:" + upperCase)
    time.sleep(2)

except KeyboardInterrupt:  
  print("Exit")
  sockTX.close()




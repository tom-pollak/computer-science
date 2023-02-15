import socket

TCP_IP = "192.168.101.1"
TCP_PORT = 8000
BUF_SIZE = 1024

sockRX = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
sockRX.bind((TCP_IP,TCP_PORT))

sockRX.listen(1)
print("RX ready")
sockConect, addr = sockRX.accept()

try:
  while True:    
    lowerCase = sockConect.recv(BUF_SIZE)
    sockConect.send(lowerCase.upper())

except KeyboardInterrupt:
  sockRX.close()

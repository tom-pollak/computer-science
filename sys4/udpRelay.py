import socket

UDP_RX_IP   = "192.168.101.1"
UDP_TX_IP   = "192.168.101.254"
UDP_RX_PORT = 8000
UDP_TX_PORT = 8001
BUF_SIZE    = 1024 

sockRX = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockRX.bind((UDP_RX_IP, UDP_RX_PORT))

sockTX = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:
  while True:
    data, addr = sockRX.recvfrom(BUF_SIZE)
    sockTX.sendto(data, (UDP_TX_IP, UDP_TX_PORT))
    print("RX message: " + str(data).strip('\n'))

except KeyboardInterrupt:
  sockRX.close()
  sockTX.close() 





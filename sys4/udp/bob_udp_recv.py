import socket

BUF_SIZE = 1024
UDP_IP = "127.0.0.1"
UDP_PORT = 8000
RECV = (UDP_IP, UDP_PORT)

sockRX = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockRX.bind(RECV)

data, _ = sockRX.recvfrom(BUF_SIZE)
FILENAME = data.decode('utf-8')

data, _ = sockRX.recvfrom(BUF_SIZE)
number_of_segments = int(data.decode('utf-8'))

with open(FILENAME, "w") as f:
    for i in range(number_of_segments):
        print(f"{i} : {len(data)}")
        data, _ =  sockRX.recvfrom(BUF_SIZE)
        f.write(data.decode('utf-8'))

import hashlib
hash = hashlib.md5(open(FILENAME, "rb").read()).hexdigest()
data, _ =  sockRX.recvfrom(BUF_SIZE)
print(hash)
assert data.decode('utf-8') == hash, "hashes do not match!"

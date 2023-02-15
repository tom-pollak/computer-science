import socket
import os

BUF_SIZE = 1024
UDP_IP = "127.0.0.1"
UDP_PORT = 8000
RECV = (UDP_IP, UDP_PORT)

FILE_PATH = "bob1.pbm"
RECV_FILE_PATH = "bob-recv.pbm"

sockTX = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sockTX.sendto(bytes(RECV_FILE_PATH, 'utf-8'), RECV)

file_size = os.path.getsize(FILE_PATH)
number_of_segments = (-(-file_size//BUF_SIZE))
sockTX.sendto(bytes(str(number_of_segments), 'utf-8'), RECV)

with open(FILE_PATH, "rb") as f:
    buffer = f.read()
    for i in range(number_of_segments):
        segment = buffer[i*BUF_SIZE: (i+1)*BUF_SIZE]
        print(f"{i} Length of segment: {len(segment)}")
import hashlib

hash = hashlib.md5(open(FILE_PATH, "rb").read()).hexdigest()
sockTX.sendto(bytes(hash, 'utf-8'), RECV)

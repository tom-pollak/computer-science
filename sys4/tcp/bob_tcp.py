import hashlib
import os
import socket

IP = "127.0.0.1"
PORT = 8000
CLIENT_ADDRESS = (IP, PORT)

HOST_FILE_PATH = "bob1.pbm"
RECV_FILE_PATH = "bob-recv.pbm"

BUF_SIZE = 1024

file_size = os.path.getsize(HOST_FILE_PATH)
number_of_segments = file_size // BUF_SIZE

headers = {
    "buf-size": BUF_SIZE,
    "recv-file-path": RECV_FILE_PATH,
    "num-segments": number_of_segments,
}

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.connect(CLIENT_ADDRESS)

    print("sending headers", headers)
    for k, v in headers.items():
        sock.sendall(f"{k}:{v}\r\n".encode("utf-8"))
    sock.sendall(f"\r\n".encode("utf-8"))

    ack = sock.recv(1024).decode("utf-8")
    assert ack == "ACK"

    with open(HOST_FILE_PATH, "rb") as f:
        buffer = f.read()
        for i in range(number_of_segments):
            segment = buffer[i * BUF_SIZE : (i + 1) * BUF_SIZE].decode("utf-8")
            sock.sendall(f"'{i}':{segment}".encode("utf-8"))

    sock.sendall(f"\r\n~~EOF~~".encode("utf-8"))

    ack = sock.recv(1024).decode("utf-8")
    assert ack == "ACK"

    hash = hashlib.md5(open(HOST_FILE_PATH, "rb").read()).hexdigest()
    sock.sendall(f"hash:{hash}".encode("utf-8"))

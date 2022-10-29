import hashlib
import re
import socket

IP = "127.0.0.1"
PORT = 8000

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
    sock.bind((IP, PORT))
    sock.listen()
    conn, addr = sock.accept()

    with conn:
        print(f"connected to {addr}")

        headers = {}
        data = ""
        while data.split("\r\n")[-2:] != ["", ""]:  # END OF HEADER BLOCK \r\n\r\n
            data += conn.recv(1024).decode("utf-8")

        headers = dict([tuple(h.split(":")) for h in data.split("\r\n")[:-2]])

        print(headers)
        conn.sendall("ACK".encode("utf-8"))

        segments = {}
        data = ""
        prev_segment = None
        while True:
            data += conn.recv(int(headers["buf-size"])).decode("utf-8")

            # Group 1: prev segment trailing data
            # Group 2: current segment id
            # Group 3: current segment data
            m = re.match(r"^(.*?)'(\d+)':(.*)", data, flags=re.DOTALL)
            if m is not None:
                if prev_segment is not None:
                    segments[prev_segment] += m.group(1)

                eof = re.match(r"^(.*?)~~EOF~~", m.group(3))
                if eof is not None:
                    segments[m.group(2)] = eof.group(1)
                    break
                else:
                    segments[m.group(2)] = m.group(3)
                prev_segment = m.group(2)
                data = ""

        conn.sendall("ACK".encode("utf-8"))

        recv_hash = conn.recv(1024).decode("utf-8").split(":")[1].strip()
        data = "".join(map(lambda x: x[1], sorted(segments.items(), key=lambda x: x[0])))
        with open(headers["recv-file-path"], "w") as f:
            f.write(data)

    bob_hash = hashlib.md5(open(headers["recv-file-path"], "rb").read()).hexdigest()
    assert bob_hash == recv_hash

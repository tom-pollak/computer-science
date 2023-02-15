import telnetlib

HOST = "192.168.59.1"
form_data = "first_name=Bob&last_name=59"

t = telnetlib.Telnet(HOST, 80, 5)
t.write("POST /cgi-bin/hello-post.cgi HTTP/1.1\r\n".encode("ascii"))
t.write("Host: pi-1\r\n".encode("ascii"))
t.write("Content-Type: application/x-www-form-urlencoded\r\n".encode("ascii"))
t.write(f"Content-Length: {len(form_data)}\r\n".encode("ascii"))

t.write("\r\n".encode("ascii"))
t.write(f"{form_data}\r\n".encode("ascii"))
t.write("\r\n".encode("ascii"))

data = ""
while data.find("</html>") == -1:
    data += (
        t.read_very_eager()
        .decode("UTF-8")
        .replace("\\n", "\n")
        .replace("\\r", "")
    )
print(data)

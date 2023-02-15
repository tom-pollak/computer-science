import telnetlib
import time
HOST = "raspberrypi-mail.local"
t = telnetlib.Telnet(HOST, 25, 5)

def telnet_query_response(query: str) -> str:
    print(query)
    t.write(f"{query}\r\n".encode("ascii"))
    time.sleep(0.5)
    res = t.read_very_eager().decode("UTF-8")
    print(f"{res}")
    return res

# Local pi mail server -- use for Q4 Wireshark
local_pi_mail = """HELO pc
mail from: pi@pi-1.local
rcpt to: pi@pi-1.local
data
Subject: test
test email from mail.py \r\n.
QUIT"""

# Raspberry pi remote mail server -- TODO: Q5
fetch_local_mail_server = """user pi
pass 12345
list
retr 1
QUIT"""

remote_mail_server = """helo pc
mail from: desk-59@raspberrypi-mail.local
rcpt to: desk-58@raspberrypi-mail.local
data
Subject:email from 59 to 58
hello test email \r\n.
QUIT"""

res = ""
for q in remote_mail_server.split("\n"):
    res += telnet_query_response(q)
print(res)


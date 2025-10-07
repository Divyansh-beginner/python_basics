import socket
import json

s = socket.socket()
s.connect(("192.168.29.110",62055))
file_name = input("enter the file name: ")
message = f"give the file : *{file_name}*"
s.send(message.encode())
file_content = []
while True:
    file_content_in_bits = s.recv(65536)
    file_content.append(file_content_in_bits)
    if file_content_in_bits == b"" : break
filecontent_inbyte = b"".join(file_content)
filecontent_injson = filecontent_inbyte.decode()
file_content = json.loads(filecontent_injson)
print(file_content)
s.close()

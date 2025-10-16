import socket
s = socket.socket()
s.connect(("",34285))
sensor_id = 10
attr_type = "temperature"
attr_value = "25.0 degree Celsius"
msg = f"{sensor_id}\r\n{attr_type}\r\n{attr_value}".encode()
s.sendall(msg)
s.close()
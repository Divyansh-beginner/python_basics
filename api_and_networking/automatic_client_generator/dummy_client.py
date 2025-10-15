import socket
s = socket.socket()
s.connect(("",34285))
sensor_id = 10
attr_type = "temperature"
attr_value = "25 degree Celsius"
msg = f"sensor_id:{sensor_id}\r\ntype:{attr_type}\r\nattribute_value:{attr_value}".encode()
s.sendall(msg)
s.close()
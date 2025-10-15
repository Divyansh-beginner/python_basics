import socket
# import sqlite3 as sql

# sql_conn = sql.connect()

def get_full_data_in_string(new_conn):
    data = b""
    while(True):
        part = new_conn.recv(1024)
        if part == b"":
            break
        data += part
    return data.decode()

with socket.socket() as s:
    s.bind(("",34285))
    s.listen()
    while True:
        new_conn , addr = s.accept()
        with new_conn:
            data = get_full_data_in_string(new_conn)
            print(data.split("\r\n"))

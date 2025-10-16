import socket
import sqlite3 as sql
import select
_sql_conn = None

def get_sql_connection():
    global _sql_conn
    if  _sql_conn is None :
        _sql_conn = sql.connect("sensors.sql")
    return _sql_conn

def get_cursor_and_make_table_if_not_made(conn):
    cur = conn.cursor()
    cur.execute('''
    create table if not exists sensors(
    id integer primary key autoincrement,
    sensor_id integer,
    sensor_type text,
    value real,
    unit text
    );
    ''')
    conn.commit()
    return cur

def add_the_data_in_sql(data):
    conn = get_sql_connection()
    cur = get_cursor_and_make_table_if_not_made(conn)
    values = data.split("\r\n")
    sensor_id = int(values[0])
    sensor_type = values[1]
    import re
    attr_value = float(re.match(r"[0-9]+\.[0-9]",values[2]).group())
    attr_unit = values[2].strip(str(attr_value))
    cur.execute('''
    insert into sensors(sensor_id,sensor_type,value,unit) values(?,?,?,?);
    ''',(sensor_id,sensor_type,attr_value,attr_unit))
    print(sensor_id,sensor_type,attr_value,attr_unit)
    conn.commit()

# --- Select-based server starts here ---
with socket.socket() as s:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("", 34285))
    s.listen()
    s.setblocking(False)  # important! non-blocking socket
    
    sockets = [s]  # track all sockets (server + clients)

    try:
        while True:
            readable, _, _ = select.select(sockets, [], [])
            for sock in readable:
                if sock is s:  # new connection
                    client_socket, addr = s.accept()
                    client_socket.setblocking(False)
                    sockets.append(client_socket)
                    print(f"New client from {addr}")
                else:  # existing client sending data
                    try:
                        data = sock.recv(1024)
                        if not data:  # client disconnected
                            print("Client disconnected")
                            sockets.remove(sock)
                            sock.close()
                        else:
                            # convert bytes to string and process
                            add_the_data_in_sql(data.decode())
                    except ConnectionResetError:
                        print("Client forcibly closed connection")
                        sockets.remove(sock)
    finally:
        if _sql_conn is not None:
            _sql_conn.close()
            

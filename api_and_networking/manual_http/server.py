import socket

def build_http_template(content)->str:
    response = (
        "HTTP/1.1 200 OK\r\n"
        +f"Content-Length: {len(content)}\r\n"
        +"Content-Type: text/plain\r\n"
        +"\r\n"
        +content
    )
    return response

def get_dict_of_headers(list_of_lines:list[str])->dict[str:str]:
    headers = {}
    flag = True
    for string in list_of_lines:
        if string == "" and flag:
            flag = False
            continue
        elif string == "" or string == list_of_lines[len(list_of_lines)-1]:
            key = "added_body"
            value = string
        else:
            key = string.split(":")[0]
            value = string.split(":")[1]
        headers[key] = value
    return headers

def greet_the_client(conn):
    main_content = "hello ✌️\n"
    response = build_http_template(main_content)
    conn.sendall(response.encode())

def respond_time_value(conn):
    import time
    obj = time.localtime()
    main_content = f"time is : {obj.tm_hour} hours and {obj.tm_min} minutes"
    response = build_http_template(main_content)
    conn.sendall(response.encode())

def echo_the_message(conn , msg):
    main_content = f"your message is : {msg}"
    response = build_http_template(main_content)
    conn.sendall(response.encode())

def handle_exit(conn):
    print("server is being closed !")
    main_content = "server is forcefully closed by exit"
    response = build_http_template(main_content)
    conn.sendall(response.encode())

def handle_invalid(conn , path):
    main_content = f"invalid request ! there is no service for {path[1:]}"
    response = build_http_template(main_content)
    conn.sendall(response.encode())

def recv_full_data_in_string(conn):
    data = b""
    while True:
        part = conn.recv(1024)
        if part is None:
            break
        data += part
    return data.decode() 

with socket.socket() as s:
    s.bind(('0.0.0.0', 58954))
    s.listen()
    print("listening now !!")
    while(True):
        new_conn , addr = s.accept()
        with new_conn:
            print(f"new request is made from {addr}")
            data = recv_full_data_in_string(new_conn)
            print(data)
            list_of_lines = data.split("\r\n")
            print("*"*55,"\n",list_of_lines)
            method , path , protocol = list_of_lines.pop(0).split(" ")
            dict_of_headers = get_dict_of_headers(list_of_lines)
            print(dict_of_headers)
            if path.strip() == "/": greet_the_client(new_conn)
            elif path.strip() == "/time": respond_time_value(new_conn)
            elif "/echo" in path : echo_the_message(new_conn , path.split("=")[1])
            elif path == "/exit" : 
                handle_exit(new_conn)
                break
            else : handle_invalid(new_conn , path)


    
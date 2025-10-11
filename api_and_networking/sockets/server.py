import socket
import json 
import os

def get_file_name_dir(data):
    start = data.find("*")+1
    end = data.rfind("*")
    filename = data.__getitem__(slice(start , end , 1))
    directory = None
    for root, dirs, files in os.walk(r"C:\Users\divya"):
        if filename in files:
            directory = os.path.join(root, filename)
            break
    return directory

def main():    
    with socket.socket() as s:
        s.bind(('0.0.0.0', 62055))
        s.listen()
        while(True):
            new_conn , addr = s.accept()
            print(f"a connection made with addr: {addr}")
            data = new_conn.recv(1024).decode()
            print("*"*50)
            print(data)
            if data.lower() == "exit" or data.lower() == "\\exit" or data.lower() == "/exit" : 
                print("server closed !")
                break
            print(data)
            file_name_dir = get_file_name_dir(data)
            with open(file_name_dir,"r",encoding="utf-8",errors="ignore") as data_to_send:
                new_conn.send(json.dumps(data_to_send.read()).encode())
            new_conn.close()

if __name__ == "__main__":main()

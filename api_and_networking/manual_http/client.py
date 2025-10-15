
def run_curl_in_terminal_only(msg):
    import os
    curl_command = f"curl http://localhost:58954/{msg}"
    os.system(curl_command)

def run_curl_to_get_response_too(msg):
    import subprocess
    response = subprocess.run(
        ["bash","-c",f"curl http://localhost:58954/{msg}"],
        text = True,
        stdout = subprocess.PIPE,
        stderr = subprocess.PIPE
    )
    data = response.stdout
    with open("text.txt","r+") as f:
        import json
        json.dump(data,f)

def run_the_command_in_terminal(msg):
    choice = input("do you want to have a way to also access the response in file , or just want to get the response in terminal ? enter 'y' for response in file , 'n' for only terminal: ")
    if choice.strip().lower() == "n" : run_curl_in_terminal_only(msg)
    else : run_curl_to_get_response_too(msg)
    
def main():
    print("select one option to request from the server")
    print("requests are: ")
    print("1. empty or only enter for greeting")
    print("2. time to get the time in 24 hour format")
    print("3. msg or message or echo to echo a message ")
    print("4. exit to end the server")
    inpu = input("enter the request: ").lower().strip()
    if inpu == "1" or inpu == "" : 
        msg = ""
    elif inpu == "2" or inpu == "time":
        msg = "time"
    elif inpu == "3" or inpu == "msg" or inpu == "message" or inpu == "echo":
        mssg = input("enter the message:").replace(" ","%20")
        msg = f"echo?msg={mssg}"
    elif inpu == "4" or inpu == "exit":
        msg = "exit"
    else :
        print("invalid input")
        return
    run_the_command_in_terminal(msg)

if __name__ == "__main__":main()
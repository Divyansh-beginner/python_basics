import socket
import threading
import time
import random

NUM_SENSORS = 10
SERVER_ADDR = "0.0.0.0"
SERVER_PORT = 34285

def get_attr_value(attr_type):
    match attr_type:
        case "temperature" : value = str(round(random.triangular(20,45,22),1))+"degree Celsius"
        case "humidity" : value = str(round(random.triangular(20.0,89.0,35.0),1))+"%"
        case "wind": value = str(round(random.triangular(0.2 , 20.0 , 8.0),1))+"m/s"
        case "altitude":value = str(round(random.triangular(100,500,300),1))+"meters"
    return value

def new_sensor(sensor_id):
    s = socket.socket()
    s.connect((SERVER_ADDR,SERVER_PORT))
    types = ["temperature","humidity","wind","altitude"]
    attr_type = random.choice(types)
    try:    
        while(True):
            attr_value = get_attr_value(attr_type)
            msg = f"sensor_id:{sensor_id}\n\rtype:{attr_type}\r\nattribute_value:{attr_value}"
            s.sendall(msg.encode())
            time.sleep(random.uniform(1,5))
    except Exception as e:
        print(f"sensor: {sensor_id} got an error:{e}")
    finally : s.close()

def main():
    for i in range(NUM_SENSORS):
        t = threading.Thread(target= new_sensor, args=(i,))
        t.daemon = True
        t.start()
        time.sleep(0.1)
    while(True):
        time.sleep(10)

if __name__ == "__main__": main()
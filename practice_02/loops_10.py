import time
max_att :int = 5
current_att:int = 1
sleep_time:int = 1
while current_att<=max_att :
    print(f"current attempt :{current_att} , sleep time : {sleep_time} secs")
    current_att += 1
    time.sleep(sleep_time)
    sleep_time *= 2


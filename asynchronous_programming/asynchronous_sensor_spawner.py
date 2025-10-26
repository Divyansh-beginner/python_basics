import asyncio as asy
import random

host = "localhost"
port = 9000

async def begin_sending_telemetry_loop(writer,id):
    writer.write(f"sensor:{id}\n".encode())
    await writer.drain()
    while True : 
        msg = f"{random.triangular(1,100,30):.2f}\n"
        writer.write(msg.encode())
        await writer.drain()
        await asy.sleep(random.triangular(1,5,3))

async def sensor_spawner(n):
    connection_task_list = []
    for id in range(n):
        open_connection_task = asy.create_task(asy.open_connection(host,port))
        open_connection_task.id = id
        connection_task_list.append(open_connection_task)
        done,_ = await asy.wait(connection_task_list,timeout=0)
        if done: 
            for task in done:
                _,writer = task.result()
                _ = asy.create_task(begin_sending_telemetry_loop(writer,task.id))
                connection_task_list.remove(task)
    while connection_task_list:
        done,_ = await asy.wait(connection_task_list,return_when=asy.FIRST_COMPLETED)
        for task in done:
            _,writer = task.result()
            _=asy.create_task(begin_sending_telemetry_loop(writer,task.id))
            connection_task_list.remove(task)
        
async def async_loop(n):
    await sensor_spawner(n)
    event = asy.Event()
    await event.wait()

def main():
    no_of_sensors = 5
    asy.run(async_loop(no_of_sensors))

if __name__ == "__main__":main()
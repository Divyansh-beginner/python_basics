import asyncio as asy
import random
async def sensor(id , runduration):
    for i in range(int(runduration)): 
        try:
            chances = int(random.triangular(10 , 50 , 15))
            flag = False
            if chances>40 : flag = True
            waittime = -1
            if flag == True : waittime = 100
            else : waittime = int(random.triangular(1,6,1))
            await asy.wait_for(asy.sleep(waittime),3)
            print(f"sensor: {id} , total runtime: {runduration} , waittime: {waittime} ")
        except asy.TimeoutError : 
            print(f"the sensor: {id} with total runtime: {runduration} and waititime: {waittime} got timed out")
    return f"sensor: {id} , total runtime: {runduration} , waittime: {waittime} , completed !"

async def create_new_tasks(task_list):
    id = 4
    for _ in range(5):
        await asy.sleep(random.triangular(1,3,1))
        task = asy.create_task(sensor(id , random.triangular(5 , 20 , 7)))
        id += 1
        task_list.append(task)

async def manager():
    async def wrapper():
        task1 = asy.create_task(sensor(1 , random.triangular(5 , 20 , 7)))
        task2 = asy.create_task(sensor(2 , random.triangular(5 , 20 , 8)))
        task3 = asy.create_task(sensor(3 , random.triangular(5 , 20 , 7)))
        tasks = [task1,task2,task3]
        _ = asy.create_task(create_new_tasks(tasks))
        while True:
            done , pending = await asy.wait(tasks,return_when=asy.FIRST_COMPLETED)
            print("beginning loop after this line")
            if not tasks: break
            for t in done: 
                try:
                    print(t.result())
                except Exception as e:
                    print(f"{t.get_name()} , failed: {e}")
            for t in pending :
                t.cancel()
                tasks.remove(t)
    await asy.wait_for(wrapper(),20)
    if wrapper.done() : create_new_tasks.cancel()

def main():
    asy.run(manager())

if __name__ == "__main__": main()
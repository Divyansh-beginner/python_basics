import asyncio as asy

async def func1(time):
    print("func1 started ")
    i = 1
    while True:
        print(f"{i}th iteration from func1")
        await asy.sleep(time)
        i += 1

async def func2(time):
    print("func2 started ")
    i = 0 
    while True:
        await asy.sleep(time)
        print(f"{i}th iteration from func2")
        i += 1

async def asynchandler():
    task1 = asy.create_task(func1(4))
    task2 = asy.create_task(func2(2))
    i = 0
    print(f"inside asynchandler {i}th iteration")
    await asy.sleep(10)
    print(f"after asynchandler {i}th iteration")
    task1.cancel()
    task2.cancel()
    result = await asy.gather(task1,task2,return_exceptions = True)
    return result

def main():
    result = asy.run(asynchandler())
    print(result)

if __name__ == "__main__":main()

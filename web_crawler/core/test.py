from fetcher import Fetcher
from config import Config
from processor import Processor
import asyncio as asy
maxsize = 5
queue = asy.Queue(maxsize= maxsize)
conobj = Config.run()
tlist = conobj.target_list
# print(tlist.pop())
fobj = Fetcher.create_fetcher_object_of_mode("fake")
probj = Processor(conobj)
# async def meth():
#     response = await fobj.fetch(tlist[0])
#     print(response)
#     await probj.process(response)
# asy.run(meth())
number_of_fetchers = 100
number_of_processors = 80
urlq = asy.Queue(maxsize=number_of_fetchers)

async def url_giver():
    for url in tlist:
        await urlq.put(url)

    # for _ in range(number_of_fetchers):
    #     await urlq.put(None)

async def fetching():
    while True:
        url = await urlq.get()
        if url is None:
            print("tlist is about to finish")
            urlq.task_done()
            return
        response = await fobj.fetch(url)
        urlq.task_done()
        await queue.put(response)

async def processing():
    while True:
        response = await queue.get()
        if response == None:
            queue.task_done()
            return
        await probj.process(response)
        queue.task_done()

async def fun():
    url_giver_task = asy.create_task(url_giver())
    fetcher_task_list = [asy.create_task(fetching()) for _ in range(number_of_fetchers)]
    
    processor_task_list = [asy.create_task(processing()) for _ in range(number_of_processors)]
    
    result_or_error = await asy.gather(url_giver_task)
    print(result_or_error)
    
    for _ in range(number_of_fetchers):
        await urlq.put(None)
    await urlq.join()
    result_or_error = await asy.gather(*fetcher_task_list , return_exceptions= True)
    print(result_or_error)
    for _ in range(number_of_processors):
        await queue.put(None)
    await queue.join()
    result_or_error = await asy.gather(*processor_task_list, return_exceptions= True)
    print(result_or_error)

asy.run(fun())
print("here10")

# obj = Fetcher.create_fetcher_object_of_mode("fake")
# endpoint = {"url":"http://localhost/search?q=cats","method":"GET"}
# response = obj.fetch(endpoint)
# print(response.headers,response.content,response.encoding,response.is_redirect,response.reason,response.url,response.status_code)

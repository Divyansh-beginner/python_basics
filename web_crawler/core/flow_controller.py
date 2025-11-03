from core.config import Config
from core.fetcher import Fetcher
from core.processor import Processor
import asyncio as asy
class Flow_controller:
    def __init__(self):
        self.config = Config.run()
        self.mode = self.config.mode
        self.fetcher_no = self.config.fetcher_no
        self.processor_no = self.config.processor_no
        self.target_list = self.config.target_list
        self.fetcher_obj = Fetcher.create_fetcher_object_of_mode(self.mode)
        self.process_obj = Processor(self.config)
        self.urlq = asy.Queue(maxsize = self.fetcher_no)
        self.responseq = asy.Queue(maxsize = self.fetcher_no)
    async def run(self):
        async def url_giver():
            for url in self.target_list:
                await self.urlq.put(url)

        async def fetcher_worker(i:int):
            print(f"{i}th fetcher starting....")
            while True:
                url = await self.urlq.get()
                if url is None:
                    self.urlq.task_done()
                    print("target_list is about to end")
                    break
                try:
                    response = await self.fetcher_obj.fetch(url)
                    await self.responseq.put(response)
                finally : self.urlq.task_done()
            print(f"{i}th fetcher ended...")

        async def processor_worker(i):
            print(f"{i}th processor starting...")
            while True:
                response = await self.responseq.get()
                if response is None:
                    self.responseq.task_done()
                    print("all urls are about to complete fetching")
                    break
                try: 
                    await self.process_obj.process(response)
                finally : self.responseq.task_done()
            print(f"{i}th processor ending...")

        url_giver_task = asy.create_task(url_giver())

        fetcher_worker_task_list = [asy.create_task(fetcher_worker(i)) for i in range(self.fetcher_no)]
        processor_worker_task_list = [asy.create_task(processor_worker(i)) for i in range(self.processor_no)]

        result_or_error = await asy.gather(url_giver_task, return_exceptions = True)
        print("url task's gather is completed",result_or_error)
        await self.urlq.join()
        for _ in range(self.fetcher_no):await self.urlq.put(None)

        result_or_error = await asy.gather(*fetcher_worker_task_list,return_exceptions= True)
        print("fether_task gather is completed",result_or_error)
        await self.responseq.join()
        for _ in range(self.processor_no): await self.responseq.put(None)

        result_or_error = await asy.gather(*processor_worker_task_list, return_exceptions = True)
        print("processor worker's gather is completed",result_or_error)


        







        

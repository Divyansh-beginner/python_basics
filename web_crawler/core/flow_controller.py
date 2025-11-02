from config import Config
from fetcher import Fetcher
from processor import Processor
import asyncio as asy
class Flow_controller:
    def __init__(self):
        self.config = Config.run()
        self.mode = self.config.mode
        self.target_list = self.config.target_list
        self.fetcher_obj = Fetcher.create_fetcher_object_of_mode(self.mode)
        self.process_obj = Processor(self.config)
        self.queue = asy.Queue(maxsize = 5)
    async def run(self):
        for endpoint in self.target_list:
            await self.queue.put(asy.create_task(self.fetcher_obj.fetch(endpoint)))
            try:
                fetched_task = self.queue.get_nowait()
                response = fetched_task.result()
                _ = asy.create_task(self.process_obj.process(response))
            except: pass



        

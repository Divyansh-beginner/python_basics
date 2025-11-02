import asyncio as asy
import random
class Processor:
    def __init__(self,config):
        self.config = config
    async def process(self,response):
        await asy.sleep(random.uniform(1,3))
        print(response.headers,response.content,response.encoding,response.is_redirect,response.reason,response.url,response.status_code)
        print("*"*44)
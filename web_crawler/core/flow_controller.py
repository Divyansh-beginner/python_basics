from config import Config
from fetcher import Fetcher
from processor import Processor

class Flow_controller:
    def __init__(self):
        self.config = Config.run()
        self.mode = self.config.mode
        self.target_list = self.config.target_list
        self.fetcher_obj = Fetcher.create_fetcher_object_of_mode(self.mode)
        self.process_obj = Processor(self.config)
    def run():
        pass

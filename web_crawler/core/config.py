class Config:
    def __init__(self,mode:str,target_list:list):
        self.mode = mode
        self.target_list = target_list
    @classmethod
    def run(cls):
        return cls(mode="fake",target_list=[])
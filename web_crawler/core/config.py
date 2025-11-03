class Config:
    def __init__(self,mode:str,target_list:list,fetcher_no:int,processor_no:int):
        self.mode = mode
        self.target_list = target_list
        self.fetcher_no = fetcher_no
        self.processor_no = processor_no
    @classmethod
    def run(cls):
        target_list = [
        # USERS
        {"url": "http://localhost/users", "method": "GET"},
        {"url": "http://localhost/users/12", "method": "GET"},
        {"url": "http://localhost/users/8", "method": "GET"},   # should 404
        {"url": "http://localhost/users", "method": "POST", "data": {"name": "Alice"}},
        
        # POSTS
        {"url": "http://localhost/posts", "method": "GET"},
        {"url": "http://localhost/posts", "method": "POST", "data": {"title": "My new post"}},
        
        # SEARCH
        {"url": "http://localhost/search?q=test_query", "method": "GET"},
        
        # REDIRECT (old endpoint)
        {"url": "http://localhost/old-endpoint/resource", "method": "GET"},
        
        # DOWNLOAD (binary)
        {"url": "http://localhost/download/file123", "method": "GET"},
        
        # PRIVATE (unauthorized)
        {"url": "http://localhost/private/data", "method": "GET"},
        
        # UNKNOWN endpoint
        {"url": "http://localhost/unknown/resource", "method": "GET"},
        ]
        return cls(mode="fake",target_list=target_list,fetcher_no =5,processor_no =3)
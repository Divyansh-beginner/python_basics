class Fetcher:

    @classmethod
    def create_fetcher_object_of_mode(cls,mode):
        if mode == "real":
           return Realfetcher()
        else : return Fakefetcher()

class Realfetcher(Fetcher):
    def fetch(self, url):
        pass
        
class Fakefetcher(Fetcher):
    def fetch(self,url):
        pass
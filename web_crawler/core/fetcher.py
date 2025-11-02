import json
import random
import asyncio as asy
class Fetcher:

    @classmethod
    def create_fetcher_object_of_mode(cls,mode):
        if mode == "real".lower()  :
           return Realfetcher()
        else : return Fakefetcher()

class Realfetcher(Fetcher):
    def fetch(self, url):
        pass
    
class Fakefetcher(Fetcher):
    @classmethod
    def give_random_name(cls,id):
        names = [
            "Avery", "Liam", "Noah", "Olivia", "Emma", "Sophia",
            "Isabella", "Mason", "Ethan", "Logan", "Lucas",
            "Mia", "Charlotte", "Amelia", "Harper", "Elijah",
            "James", "Benjamin", "Alexander", "Henry", "Evelyn",
            "Ella", "Aria", "Scarlett", "Grace", "Chloe", "Daniel",
            "Jack", "Sebastian", "Zoe", "Luna", "Layla", "Hazel",
            "Leo", "Owen", "Aiden", "Wyatt", "Nora", "Isla", "Stella"
        ]
        return random.choice(names) + f"_{id}"
    
    @classmethod
    def generate_email(cls,name,id):
        suffix = random.randint(1000,9999)
        name = name.split("_")[0]
        return f"{id}{name}_{suffix}@gmail.com"
    
    async def fetch(self,endpoint={}):
        """endpoint is a dict like:
           {"url": "...", "method": "GET", "data": {...}}
        """
        await asy.sleep(random.uniform(0.3,1.2))
        url = endpoint.get("url", "")
        method = endpoint.get("method", "GET").upper()
        data = endpoint.get("data")

        # Base headers
        headers = {}
        server = url.removeprefix("https://").partition("/")[0] if url.startswith("https") else url.removeprefix("http://").partition("/")[0]
        headers["Server"] = server

        # Default values
        status_code = 200
        reason = "OK"
        body = {}
        content_type = "application/json"

        # --------------------------
        # USERS endpoint
        # --------------------------
        if "users" in url:
            headers["Content-Type"] = content_type

            if method == "GET":
                try:
                    user_no = int(url.rstrip("/").split("/")[-1])
                    if user_no > 10:
                        name = self.__class__.give_random_name(user_no)
                        email = self.__class__.generate_email(name,user_no)
                        body = {
                            "id": user_no,
                            "name": name,
                            "email": email,
                        }
                    else:
                        status_code = 404
                        reason = "Not Found"
                        body = {"error": "User not found", "code": 404}
                except ValueError:
                    # e.g., GET /users (no specific ID)
                    body = []
                    for i in range(11,16):
                        name = self.__class__.give_random_name(i)
                        email = self.__class__.generate_email(name,i)
                        body.append({"id":i, "name":name, "email":email})

            elif method == "POST":
                new_id = random.randint(100, 999)
                status_code = 201
                reason = "Created"
                body = {
                    "id": new_id,
                    "name": data.get("name", f"User{new_id}"),
                    "status": "created",
                }

        # --------------------------
        # POSTS endpoint
        # --------------------------
        elif "posts" in url:
            headers["Content-Type"] = content_type
            if method == "GET":
                body = [{"post_id": i, "title": f"Post {i}", "author": self.__class__.give_random_name(i)} for i in range(1, 6)]
            elif method == "POST":
                new_id = random.randint(50, 200)
                status_code = 201
                reason = "Created"
                body = {"post_id": new_id, "title": data.get("title", f"Post {new_id}"), "status": "created"}

        # --------------------------
        # SEARCH endpoint
        # --------------------------
        elif "search" in url:
            query = url.partition("?q=")[-1]
            body = {"query": query, "results": [self.__class__.give_random_name(i) for i in range(1, 4)]}

        # --------------------------
        # OLD endpoint (simulate redirect)
        # --------------------------
        elif "old-endpoint" in url:
            status_code = 301
            reason = "Moved Permanently"
            headers["Location"] = url.replace("old-endpoint", "new-endpoint")
            body = {"message": "Resource moved"}

        # --------------------------
        # DOWNLOAD endpoint
        # --------------------------
        elif "download" in url:
            headers["Content-Type"] = "application/octet-stream"
            body = b"This would be binary file data"
            return Fakeresponse(url, status_code, reason, headers, body)

        # --------------------------
        # PRIVATE endpoint (unauthorized)
        # --------------------------
        elif "private" in url:
            status_code = 403
            reason = "Forbidden"
            body = {"error": "Access denied"}

        # --------------------------
        # Default fallback
        # --------------------------
        else:
            status_code = 404
            reason = "Not Found"
            body = {"error": "Unknown endpoint"}

        # Encode JSON body (if dict)
        body_bytes = body if isinstance(body, (bytes, bytearray)) else json.dumps(body).encode("utf-8")

        return Fakeresponse(url, status_code, reason, headers, body_bytes)
        return Fakeresponse(url)

class Fakeresponse:
    def __init__(self,url="",status_code = 200,reason = "OK",headers=None,encoding = "utf-8",body = b"",is_redirect = False):
        self.reason = reason
        self.status_code = status_code
        self.content = body
        try:
            self.text = self.content.decode()
        except:
            self.text = ""
        self.headers = headers or {}
        self.encoding = encoding
        self.url = url
        self.is_redirect = is_redirect
        self.ok = True if (self.status_code<400 and self.status_code>=200) else False

    def json(self):
        try:
            py_obj = json.loads(self.text)
        except Exception : 
            print("exception occured")
            return None
        else: return py_obj
       
    
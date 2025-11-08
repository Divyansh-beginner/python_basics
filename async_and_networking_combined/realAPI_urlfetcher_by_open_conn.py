import asyncio as asy
import ssl
from urllib.parse import urlparse
from target_list import target_list

def httpwrapper(urldict):
    link:str = urldict["url"]
    method:str = urldict["method"]
    parsed_link_obj = urlparse(link)
    protocol = parsed_link_obj.scheme
    ssl_ctx = ssl.create_default_context() if protocol == "https" else None
    host = parsed_link_obj.netloc
    path = parsed_link_obj.path or "/"
    if parsed_link_obj.query:
        path += "?" + parsed_link_obj.query
    port = 443 if ssl_ctx else 80
    ip = (host, port)
    first_request_line = f"{method} {path} HTTP/1.1\r\n"
    headers = (
        f"HOST: {host}\r\n"
        f"Accept: */*\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )
    full_request_string = first_request_line+headers
    return (ip,ssl_ctx,full_request_string)

async def fetcher(urldict:dict):
    ip,ssl_ctx,request_string = httpwrapper(urldict)
    reader, writer = await asy.open_connection(*ip, ssl =ssl_ctx)
    writer.write(request_string.encode())
    await writer.drain()
    raw_response = await reader.read()
    response = raw_response.decode()
    writer.close()
    await writer.wait_closed()
    return response

async def asynclooper():
    task_list = [asy.create_task(fetcher(urldict)) for urldict in target_list]
    result_list = await asy.gather(*task_list,return_exceptions = True)
    for i,result in enumerate(result_list):
        print("*"*110)
        print(f"{i}...response>: {result}")

asy.run(asynclooper())







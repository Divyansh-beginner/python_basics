import asyncio as asy
import time
sensors_list = {}

async def handle_conn(reader,writer):
    try:
        addr = writer.get_extra_info('peername')
        print(f"connection was made with {addr}")
        mssg = (await reader.readline()).decode()
        try:
            id = int(mssg.split(":")[1])
            sensors_list[f"sensor:{id}"] = {"addr":addr,"id":id,"connection_time":time.localtime()}
        except Exception as e :
            print(f"the sensor was unable to send credentials, closing the connection with it")
            return
        while True: 
            mssg_in_bits = await reader.readline()
            mssg = mssg_in_bits.decode()
            if not mssg : 
                print(f"sensor:{id} is closed")
                writer.close()
                await writer.wait_closed()
                break
            try:
                print(f"value:{float(mssg)},from sensor:{id}")
            except: pass
    except Exception as e :
        print("*"*55,f"the server was shutdown, error:{e}")
        return

async def server():
    print("server started")
    server_obj = await asy.start_server(handle_conn,"localhost" , 9000)
    async with server_obj:
        await server_obj.serve_forever() 

def main():
    asy.run(server())

if __name__ == "__main__" : main()
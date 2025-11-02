from core.flow_controller import Flow_controller
import asyncio as asy

async def main():
    flow_controller_starter_obj = Flow_controller()
    await flow_controller_starter_obj.run()

if __name__ == "__main__":
    asy.run(main())
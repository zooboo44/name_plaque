import time
import asyncio
from graph import Graph
from pathlib import Path
from led_control import LedControl
import os

graph: Graph = Graph(".env")

if not Path(".auth_record").exists():
    graph.authenticate()



led_control = LedControl(".env")

async def main():
    while True:
        user_status = await graph.get_presence()
        led_control.set_color(user_status)
        time.sleep(2)

if __name__ == '__main__':
    asyncio.run(main())

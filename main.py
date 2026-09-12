import time
import asyncio
from graph import Graph
from pathlib import Path

graph: Graph = Graph(".env")

if not Path(".auth_record").exists():
    graph.authenticate()

async def main():
    while True:
        await graph.print_presence()
        time.sleep(10)

if __name__ == '__main__':
    asyncio.run(main())

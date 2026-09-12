from graph import Graph
from pathlib import Path
import asyncio

graph: Graph = Graph(".env")

if not Path(".auth_record").exists():
    graph.authenticate()

async def main():
    await graph.print_presence()

if __name__ == '__main__':
    asyncio.run(main())

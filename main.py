from graph import Graph
import asyncio

grpah : Graph = Graph(".env")

async def main():
    await grpah.print_presence()

if __name__ == '__main__':
    asyncio.run(main())

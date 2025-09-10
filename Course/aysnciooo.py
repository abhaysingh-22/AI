import asyncio

async def main():
    print("Hello, Asyncio!")
    await asyncio.sleep(1)
    print("Goodbye, Asyncio!")
    
asyncio.run(main())
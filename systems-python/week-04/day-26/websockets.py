import asyncio
import websockets

async def handler(websocket):
    print("A client connected")

async def main():
    server = await websockets.serve(handler, "localhost", 8765)
    await server.wait_closed()

asyncio.run(main())
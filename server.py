import asyncio
import websockets

async def echo(websocket, path):
    async for message in websocket:
        # Echo the received message back to the client
        await websocket.send(message)

start_server = websockets.serve(echo, "localhost", 8765)

async def main():
    async with start_server:
        await start_server.serve_forever()

asyncio.run(main())

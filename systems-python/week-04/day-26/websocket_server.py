import asyncio
import websockets
import json
from datetime import datetime

connected_clients = set()

async def handle_client(websocket):
    connected_clients.add(websocket)
    print(f"Client connected. Total: {len(connected_clients)}")
    
    try:
        async for message in websocket:
            data = json.loads(message)
            print(f"Received: {data}")
            
            # Broadcast to all connected clients
            response = {
                "type": "message",
                "content": data.get("content", ""),
                "timestamp": datetime.now().isoformat()
            }
            
            websockets.broadcast(connected_clients, json.dumps(response))
    
    except websockets.exceptions.ConnectionClosed:
        print("Client disconnected")
    finally:
        connected_clients.discard(websocket)
        print(f"Client removed. Total: {len(connected_clients)}")

async def main():
    print("WebSocket server starting on ws://localhost:8765")
    async with websockets.serve(handle_client, "localhost", 8765):
        await asyncio.Future()  # run forever

asyncio.run(main())
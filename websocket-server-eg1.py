import asyncio
import websockets

connected_clients = set()

async def handle_client(websocket):
    connected_clients.add(websocket)

    try:
        # continuously checks for any messages
        async for message in websocket:
            print(f"Message: {message}")

            response = f"Message received: {message}"
            await websocket.send(response)

            # checks if the client is there
            for client in connected_clients:
                # sends the message to all the clients except the one who is sending it i.e., websocket
                if client != websocket:
                    await client.send(message)
    except websockets.exceptions.ConnectionClosed:
        pass
    finally:
        connected_clients.remove(websocket)

async def main():
    server = await websockets.serve(handle_client, 'localhost', 12345)
    await server.wait_closed()

if __name__ == '__main__':
    asyncio.run(main())
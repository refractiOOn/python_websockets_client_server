import asyncio
import websockets


PORT = 8080
connected = set()


async def echo(websocket, path) -> None:
    print('Client connected')
    connected.add(websocket)
    try:
        async for message in websocket:
            print(f'Received message: {message}')
            for conn in connected:
                if conn == websocket:
                    continue
                await conn.send(f'Someone said: {message}')

    except websockets.exceptions.ConnectionClosed as ex:
        print('Client disconnected')
    finally:
        connected.remove(websocket)


def main() -> None:
    print(f'Server listening on port {PORT}')
    
    start_server = websockets.serve(echo, 'localhost', PORT)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()


if __name__ == '__main__':
    main()

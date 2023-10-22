import websockets
import asyncio


async def listen() -> None:
    url = 'ws://127.0.0.1:8080'
    async with websockets.connect(url) as ws:
        await ws.send('Hello server!')
        while True:
            message = await ws.recv()
            print(f'Received message: {message}')


def main() -> None:
    asyncio.get_event_loop().run_until_complete(listen())


if __name__ == '__main__':
    main()
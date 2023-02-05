import asyncio

HOST = '0.0.0.0'
PORT = 5454

WRITERS = set()


async def handle_echo(reader, writer):
    WRITERS.add(writer)

    while True:
        try:
            data = await reader.read(1024)
            message = data.decode()
            addr = writer.get_extra_info('peername')
            if not data:
                writer.close()
                print(f"{addr!r} close the connection")
                break

            for w in WRITERS:
                if w == writer:
                    print(f"Received {message!r} from {addr!r}")
                    continue
                w.write(data)
            await asyncio.gather(*(w.drain() for w in WRITERS if w != writer))
        except ConnectionResetError:
            writer.close()


async def main():
    server = await asyncio.start_server(
        handle_echo, HOST, PORT)

    addrs = ', '.join(str(sock.getsockname()) for sock in server.sockets)
    print(f'Serving on {addrs}')

    async with server:
        await server.serve_forever()

asyncio.run(main())

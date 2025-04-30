import asyncio
import websockets

clients = {}  # websocket: nickname

async def handler(websocket):
    await websocket.send("Введите никнейм:")
    nickname = await websocket.recv()

    # Проверка на уникальность
    if nickname in clients.values():
        await websocket.send("Никнейм уже занят. Перезагрузите страницу.")
        await websocket.close()
        return

    clients[websocket] = nickname
    await broadcast(f"🔵 {nickname} присоединился к чату.")

    try:
        async for message in websocket:
            await broadcast(f"{nickname}: {message}")
    except:
        pass
    finally:
        await broadcast(f"🔴 {nickname} покинул чат.")
        del clients[websocket]

async def broadcast(message):
    to_remove = []
    for ws in clients:
        try:
            await ws.send(message)
        except:
            to_remove.append(ws)
    for ws in to_remove:
        del clients[ws]

# Создаём и запускаем цикл событий
async def main():
    start_server = await websockets.serve(handler, "localhost", 8765)
    print("Сервер запущен на ws://localhost:8765")
    await start_server.wait_closed()

# Запускаем основной цикл
if __name__ == "__main__":
    asyncio.run(main())

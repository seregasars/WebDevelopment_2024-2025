import socket

HOST = '127.0.0.1'  # IP адрес сервера (в локальной сети или 127.0.0.1)
PORT = 65432        # Порт (должен совпадать с портом сервера)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))             # Подключаемся к серверу
    s.sendall(b'Hello, server')         # Отправляем сообщение
    data = s.recv(1024)                 # Получаем ответ
    print('Ответ от сервера:', data.decode())

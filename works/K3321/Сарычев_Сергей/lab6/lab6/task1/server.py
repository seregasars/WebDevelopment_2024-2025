import socket

HOST = '127.0.0.1'  # Локальный хост
PORT = 65432        # Порт (должен быть тот же, что и у клиента)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))         # Привязываем сокет к хосту и порту
    s.listen()                   # Слушаем входящие подключения
    print('Сервер запущен, ожидаем подключение...')

    conn, addr = s.accept()      # Принимаем подключение
    with conn:
        print('Подключено к', addr)
        data = conn.recv(1024)   # Получаем данные
        print('Получено сообщение от клиента:', data.decode())

        conn.sendall(b'Hello, client')  # Отправляем ответ

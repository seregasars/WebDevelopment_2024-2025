import socket
import os

HOST = '127.0.0.1'
PORT = 8080

with open('task3/index.html', 'r', encoding='utf-8') as file:
    html_content = file.read()

# Преобразуем в байты заранее, чтобы корректно посчитать длину
html_bytes = html_content.encode('utf-8')

# Формируем корректный HTTP-ответ
http_response = b"".join([
    b"HTTP/1.1 200 OK\r\n",
    b"Content-Type: text/html; charset=utf-8\r\n",
    f"Content-Length: {len(html_bytes)}\r\n".encode(),
    b"\r\n",  # Пустая строка — разделение заголовков и тела
    html_bytes
])

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print(f"Сервер запущен на http://{HOST}:{PORT}")

    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Клиент подключился: {addr}")
            request = conn.recv(1024).decode()
            print("Запрос клиента:")
            print(request)

            conn.sendall(http_response)

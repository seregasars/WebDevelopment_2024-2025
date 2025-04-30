import socket

HOST = '127.0.0.1'
PORT = 65432

# Ввод данных
a = input('Введите катет a: ')
b = input('Введите катет b: ')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    message = f'{a},{b}'
    s.sendall(message.encode())

    data = s.recv(1024).decode()
    print('Ответ от сервера:', data)

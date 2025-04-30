import socket
import math

HOST = '127.0.0.1'
PORT = 65432

def calculate_hypotenuse(a, b):
    return math.sqrt(a**2 + b**2)

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    print('Сервер запущен, ожидаем подключение...')

    conn, addr = s.accept()
    with conn:
        print('Подключено к', addr)
        data = conn.recv(1024).decode()
        print('Получено:', data)

        try:
            a_str, b_str = data.split(',')
            a = float(a_str)
            b = float(b_str)
            c = calculate_hypotenuse(a, b)
            result = f'Гипотенуза: {c:.2f}'
        except Exception as e:
            result = f'Ошибка вычислений: {e}'

        conn.sendall(result.encode())

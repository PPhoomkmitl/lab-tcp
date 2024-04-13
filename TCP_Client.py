import socket

HOST = '172.10.20.12'
PORT = 2059

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

client_name = input("Enter your name: ")

while True:
    try:
        client_input = input("Enter something: ")
        client_socket.sendall(f'{client_name} : {client_input}'.encode('utf-8'))

        data = client_socket.recv(1024).decode('utf-8')
        print(f'Received data from: {data}')

        if data.lower() == 'exit':
            break
    except KeyboardInterrupt:
        print("You didn't respond in time. Connection terminated.")
        break

client_socket.close()
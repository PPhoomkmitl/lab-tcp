from socket import *

HOST = '172.20.10.12'
PORT = 2059
# Hostname = socket.getJost 

server_socket = socket(AF_INET, SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f'Server is listening on {HOST}:{PORT}...')

while True:
    try:
        connection_socket, client_address = server_socket.accept()
        print(f'Client {client_address} connected.')

        while True:
            data = connection_socket.recv(2048).decode()
            if not data:
                break
            print(f'Received data from {data}')

            server_input = input("Enter something (type 'exit' to quit): ")
            if server_input.lower() == 'exit':
                break
            connection_socket.send(server_input.encode('utf-8'))

        connection_socket.close()
        print(f'Client {client_address} disconnected.')

    except KeyboardInterrupt:
        print("You didn't respond in time. Connection terminated.")
        break

server_socket.close()
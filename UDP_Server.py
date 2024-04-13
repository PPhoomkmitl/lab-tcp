from socket import *

HOST = '172.20.10.12'
PORT = 2059

server_socket = socket(AF_INET, SOCK_DGRAM)
server_socket.bind((HOST, PORT))

print(f'Server is listening on {HOST}:{PORT}...')

while True:
    try:
        data, client_address = server_socket.recvfrom(2048)
        print(f'Received data from {data.decode()}')

        server_input = input("Enter something (type 'exit' to quit): ")
        if server_input.lower() == 'exit':
            break
        server_socket.sendto(server_input.encode(), client_address)

    except KeyboardInterrupt:
        print("You didn't respond in time. Connection terminated.")
        break

server_socket.close()
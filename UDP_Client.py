from socket import * 
import time

HOST = '17.ip.gl.ply.gg'
PORT = 2059

client_socket = socket(AF_INET, SOCK_DGRAM)

client_name = input("Enter your name: ")

while True:
    try:
        client_input = input("Enter something: ")
        if client_input == 'exit':
            break
        
        client_socket.sendto(f'{client_name} : {client_input}'.encode(), (HOST, PORT))
        data, server_address = client_socket.recvfrom(2048)
        print(f'Received data from Server: {data.decode()}')

    except KeyboardInterrupt:
        print("You didn't respond in time. Connection terminated.")
        break

client_socket.close()
from socket import *
serverPort = 2059
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('172.20.10.12', serverPort))
print('The server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    print(message)
    serverSocket.sendto(modifiedMessage.encode(),clientAddress)
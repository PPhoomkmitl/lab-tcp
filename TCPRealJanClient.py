from socket import *
serverName = '172.20.10.12'
serverPort = 2059
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName,serverPort))

while True:
    sentence = input('Input lowercase sentence:')
    clientSocket.send(sentence.encode())
    modifiedSentence = clientSocket.recv(1024)
    print ('From Server:', modifiedSentence.decode())
    clientSocket.close()
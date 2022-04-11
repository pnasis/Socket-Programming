from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort))
print('The server is ready to receive questions')
while True:
    question, clientAddress = serverSocket.recvfrom(1024)
    print('Question received from ', clientAddress, ": ", question.decode())
    response = input('Enter answer to send to client: ')
    serverSocket.sendto(response.encode(), clientAddress)
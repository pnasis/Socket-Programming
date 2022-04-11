from socket import *
serverName = '127.0.0.1'
serverPort = 12000
clientSocket = socket(AF_INET, SOCK_DGRAM)
#clientSocket.connect((serverName, serverPort))
question = input('Input lowercase sentence: ')
clientSocket.sendto(question.encode(), (serverName, serverPort))
answer, serverAddress = clientSocket.recvfrom(1024)
if serverAddress == (serverName, serverPort):
    print('The answer is: ', answer.decode())
else:
    print('ALERT! Received message from unknown server')
clientSocket.close()
from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) #Sock_Stream = we set that we will work with a tcp socket.
serverSocket.bind(('', serverPort))
serverSocket.listen(1) #We can receive and keep in a queue up to 1 tcp request.

print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept() #Waiting to accept the request.
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()

#When we try to establish a new connection, a new connectionSocket will be created.

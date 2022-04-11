from socket import *
ClientName = 'localhost'
ClientPort = 33316 #Το Port το βρήσκουμε μέσω του UDPClient.
message = 'boo'
clientSocket = socket(AF_INET, SOCK_DGRAM)
clientSocket.sendto(message.encode(), (ClientName, ClientPort))
clientSocket.close()
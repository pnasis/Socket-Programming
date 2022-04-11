from socket import *
serverPort = 12000 #Είναι καλό για testing να βάζω τόσο μεγάλο port
serverSocket = socket(AF_INET, SOCK_DGRAM)
serverSocket.bind(('', serverPort)) # '' = οποιαδήποτε διεύθυνση. Ορίζουμε στο λειτουργικό να ακούει στο port 12000.
print('The server is ready to receive')
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper() #Μετατρέπω το μήνυμα σε κωδικούς Ascii και στην συνέχεια σε κεφαλαία.
    serverSocket.sendto(modifiedMessage.encode(), clientAddress) #Πάρε το μήνυμα, κωδικοποίησέ το και στείλτο στο client address.

# SOCK_DGRAM = είναι παράμετρος που δηλώνει πως θα χρησιμοποιήσουμε πρωτόκολλο UDP
# Γραμμή 7: i)message, clientAddress = διάβασε το μήνυμα και τη διεύθυνση από τον χρήστη.
#          ii)serverSocket.recvfrom(2048) = περιμένω να διαβάσω μέχρι 2048 bits.
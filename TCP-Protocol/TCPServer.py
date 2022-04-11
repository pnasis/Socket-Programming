from socket import *
serverPort = 12000
serverSocket = socket(AF_INET, SOCK_STREAM) #Sock_Stream = ορίζουμε ότι θα είναι socket tcp
serverSocket.bind(('', serverPort))
serverSocket.listen(1) #μπορώ να λάβω και να κρατήσω σε μια ουρά μέχρι 1 αίτημα tcp
print('The server is ready to receive')
while True:
    connectionSocket, addr = serverSocket.accept() #περιμένει να αποδεχθεί το αίτημα για σύνδεση.Δημιουργεί μια νέα socket που είναι το άκρο της εξυπηρέτησης για τη συγκεκριμένη σύνδεση.
    sentence = connectionSocket.recv(1024).decode()
    capitalizedSentence = sentence.upper()
    connectionSocket.send(capitalizedSentence.encode())
    connectionSocket.close()

#Όταν επιχειρήσω νέα σύνδεση θα δημιουργηθεί εξαρχής καινούργιο connectionSocket.

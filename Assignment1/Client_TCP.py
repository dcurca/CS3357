# Dana Curca 250976773
# Client_TCP that sends a message to a server, the client waits for the server to respond when given valid input


from socket import *
#establishing server information
serverName = '127.0.0.1'
serverPort = 12000
print("Attempting to contact server at ", serverName, ":" , serverPort)
clientSocket = socket(AF_INET, SOCK_STREAM)
#error checking to make sure server connection is established
try:
    clientSocket.connect((serverName, serverPort))
    print("Connection to server established")
except Exception as e:
    #if server connection is not established close client and quit program
    print("Error connecting to server")
    clientSocket.close()
    quit()
#once connection is established necessary data transfer begins
sentence = "What is the current date and time?"
clientSocket.send(sentence.encode())
modifiedSentence = clientSocket.recv(1024)
#print data sent from server
print("From Server:", modifiedSentence.decode())
clientSocket.close()

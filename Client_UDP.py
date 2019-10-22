# Dana Curca 250976773
# Client_UDP class that sends data to a server and waits for a response for a valid input

from socket import *
#establishing server information
serverName = '127.0.0.1'
serverPort = 12000
#error checking to make sure server connection is established
try:
    #once established move onto the necessary data transfer
    clientSocket = socket(AF_INET, SOCK_DGRAM)
except Exception as e:
    #if server connection is not established close client and quit program
    print("Error connecting to server")
    clientSocket.close()
    quit()
#sending message to server and waiting for response back
message = "What is the current date and time?"
clientSocket.sendto(message.encode(),(serverName, serverPort))
modifiedMessage, serverAddresss = clientSocket.recvfrom(2048)
#print data sent from server
print(modifiedMessage.decode())
clientSocket.close()
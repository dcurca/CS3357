# Dana Curca 250976773
# Server_TCP that listens and waits for a connection with a client and upon connection recieves data
# server gives correct response back to client and only responds when valid input is given

from socket import *
import time
#establishing corresponding server information with client
serverPort = 12000
try:
    #error checking to make sure server is ready and listening for client
    serverSocket = socket(AF_INET, SOCK_DGRAM)
    serverSocket.bind(('', serverPort))
    print("The server is ready to recieve")
except Exception as e:
    #if server is not ready or listening the server failed to create itself and quits the program
    print("Error attempting to create server")
    serverSocket.close()
    quit()
#once server is successfully created and listening, it waits for client to send data
while True:
    message, clientAddress = serverSocket.recvfrom(2048)
    modifiedMessage = message.decode().upper()
    #error checking for correct data from client
    if modifiedMessage == "WHAT IS THE CURRENT DATE AND TIME?":
        datetime = "Current Date and Time - " + time.strftime('%m/%d/%Y %H:%M:%S')
    else:
        #if data is not expected data, unexpected return message is given
        datetime = "Invalid argument, please try again"

    serverSocket.sendto(datetime.encode(), clientAddress)
    #after server sends correct or incorrect response back to client the server breaks from sending loop and closes program
    break
serverSocket.close()

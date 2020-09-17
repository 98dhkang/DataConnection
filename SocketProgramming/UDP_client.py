# UDP client

from socket import *

serverName='192.168.219.199'
serverPort=12000

clientSocket=socket(AF_INET,SOCK_DGRAM)

message=input('Input lowercase sentence : ')

clientSocket.sendto(message.encode(),(serverName, serverPort))

modifiedMessage, serverAddress = clientSocket.recvfrom(2048)

print('From UDP server:',modifiedMessage.decode())

clientSocket.close()


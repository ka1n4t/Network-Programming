#!/usr/bin/python

from socket import *

serverPort = 12345
server_socket = socket(AF_INET,SOCK_STREAM)
server_socket.bind(('',serverPort))

server_socket.listen(1)
while True:
	server_conn, client_addr = server_socket.accept()
	message = server_conn.recv(1024)
	response = 'I have received your message:\n'+message+'\nAm I smart? hhhh'
	server_conn.send(response)
	server_conn.close()

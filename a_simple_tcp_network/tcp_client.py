#!/usr/bin/python

from socket import *

server_address = '10.10.10.132'
server_port = 12345

client_connect = socket(AF_INET, SOCK_STREAM)
client_connect.connect((server_address, server_port))

message = raw_input('Input some words you wanna send to your server: ')
client_connect.send(message)

response = client_connect.recv(4096)
print('[+]Server Responding: %s [+]' % response)

client_connect.close()

"""
    Same as webserver3c but in this one the parent and child processes DO NOT close duplicate descriptors
"""

import socket
import time
import os

SERVER_ADDRESS = (HOST, PORT) = '', 1028
REQUEST_QUEUE_SIZE = 5

def handle_request(client_connection):
    request = client_connection.recv(1024)
    http_response = b"""\
HTTP/1.1 200 OK

Hello, World!
"""
    client_connection.sendall(http_response)

def serve_forever():
    listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listen_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR, 1)
    listen_socket.bind(SERVER_ADDRESS)
    listen_socket.listen(REQUEST_QUEUE_SIZE)
    print('Serving HTTP on port {port} ...'.format(port= PORT))

    clients = []

    while True:
        client_connection, client_address = listen_socket.accept()
        clients.append(client_connection)
        pid = os.fork()
        if pid == 0: #child
            listen_socket.close() #child copy
            handle_request(client_connection)
            client_connection.close()
            os._exit(0) #child exists here
        else: #Parent
            # client_connection.close()
            print(len(clients))
if __name__ == '__main__':
    serve_forever()
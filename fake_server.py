import socket

def main():

    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    host = '0.0.0.0'
    port = 3333
    server_socket.bind((host, port))
    server_socket.listen()
    
    while True:
        client_socket, client_address = server_socket.accept()
        response = client_socket.recv(1024)
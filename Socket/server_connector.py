import socket
import json

class Client:

    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

    def connection(self):
        while True:
            # Creates a socket
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.client_socket.connect((self.host, self.port))

            response = json.loads(self.client_socket.recv(2048).decode())

            if response == 'ping':
                print('ping')
                self.client_socket.send(json.dumps({"response": "pong"}))

    def send_message(self, message: dict)->None:
        # Connect to the server
        self.connection()  
        # Send the message to the server
        self.client_socket.send(json.dumps(message).encode())  

client1 = Client('127.0.0.1', 3000)
message = {"request": "subscribe",
           "port": 3000,
           "name": "Madame_Henrotte_gaming",
           "matricules": ["23363", "23049"]
           }
client1.send_message(message)
        
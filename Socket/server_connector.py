import socket
import json

class Client:

    def __init__(self, host, port) -> None:
        self.host = host
        self.port = port

    def connect(self, message: dict):
        
        try: # Connect to the server
            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.s.connect((self.host, self.port))
            print('Client connected')  
            # Send the message to the server
            self.s.send(json.dumps(message).encode())
            print('Connection request sent')  

            while True:

                try:
                    response = (self.s.recv(4000).decode())
                    response = json.loads(response)

                    if response["response"] == "ping":
                        self.s.send(json.dumps({"response": "pong"}))
                        print('pong')
                    else:
                        print(f'Server response {response}')
                except:
                    pass
        except ConnectionRefusedError as e:
            print(f'Connection failed: {e}')
            

client1 = Client('127.0.0.1', 3000)
message = {"request": "subscribe",
           "port": 4000,
           "name": "Madame_Henrotte_gaming",
           "matricules": ["23363", "23049"]
           }
client1.connect(message)
        
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
            self.message_sender(message)

            while True:

                try:
                    response = (self.s.recv(4000).decode())
                    response = json.loads(response)
                    self.response_treatment(response)
                except:
                    pass
        except ConnectionRefusedError as e:
            print(f'Connection failed: {e}')
    
    def response_treatment(self, response): #quand un message est reçu ceci est le centre de traitement

        if response["response"] == "ping": #réponse ping pong
            self.message_sender({"response": "pong"})

        elif response["response"] == "play": #réponse de coup
            print(response["state"])
            try:
                self._message = random_play(response["state"])
                self.message_sender(self._message)
            except: #si le coup est raté voici ce qu'on envoie au pire des cas
                self.message_sender({"response": "giveup"})
        else: #en cas d'autre message, on le print
            print(f'Server response {response}')
    
    def message_sender(self, message): #manière ordonnée d'envoyer les messages au serveur. Tout les messages reçus sont des bibliothèques et traités ensuite en json
        try:
            self.s.send(json.dumps(message).encode())
        except Exception as e:
            print(f'Message not sent : {e}')
            

client1 = Client('172.17.10.133', 3000)
message1 = {"request": "subscribe",
           "port": 4000,
           "name": "Henrotte/Redbull",
           "matricules": ["23363", "23049"]
           }

client1.connect(message1)

        
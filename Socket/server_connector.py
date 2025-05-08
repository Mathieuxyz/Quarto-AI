import socket

import json

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import dataclass_pooling as dcp


class Client: #We will first connect the client to the server to subscribe himself to the contest and only then he will shift to player mode with another port


    def __init__(self, host, port, message): #To NOT modify !
        
        self.host = host
        
        self.port = port
        
        self.message = message
        
        self.subscribe()


    def subscribe(self): #We will first connect the client to the server to subscribe himself to the contest

        try: # Connect to the server

            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP connnection

            self.s.connect((self.host, self.port))

            # Send the message to the server

            self.s.send(json.dumps(self.message).encode())

            self.s.close() 

            print(f'Client {self.message["name"]} is subscribed to the server') #confirmation message

            self.connect_game()


        except ConnectionRefusedError as e: #in case a connection failed

            print(f'Connection failed: {e}')



    def connect_game(self): #connecting the new socket to play on a new port
        
        try: # Connect to the server

            self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #TCP connection

            self.s.bind(('0.0.0.0', self.message["port"]))

            self.s.listen()

            while True: #Once the socket is connected, this While True makes sures all the messages are received

                try:

                    self.client, self.adress = self.s.accept()
                    
                    response = self.client.recv(1024)

                    response = json.loads(response)

                    self.response_treatment(response)

                    self.client.close()

                except:

                    pass

        except Exception as e: #in case a connection failed

            print(f'Connection failed: {e}')


    def response_treatment(self, response): #This is like a centre were all received messages from the server are managed

        print(response)

        if response["request"] == "ping": #ping pong response

            self.message_sender({"response": "pong"})
            print('pong')

        elif response["request"] == "play": #play response

            try:

                ai = dcp.quartoAI(response["state"])
                self._message = dcp.ai.move() #call to the win document that manages game startegy

                response = {"response": "move", "move": self._message, "message": "La calotte de tes morts"}
                self.message_sender(response)

            except: #if nothing works, we give up the game

                self.message_sender({"response": "giveup"})

        else: #if another message is received

            print(f'Server response {response}')


    def message_sender(self, message): #Organised way to send the messages. The function receives a dictionnary and transform it in a sendable message

        try:

            self.client.sendall(json.dumps(message).encode())

        except Exception as e:
        
            print(f'Message not sent : {e}')
            


message = {"request": "subscribe",
           "port": 4000,
           "name": "Tartiflette",
           "matricules": ["23363", "23049"]
           }
client = Client('172.17.10.133', 3000, message)
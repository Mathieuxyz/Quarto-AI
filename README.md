# Quarto-AI

## Project Overview

This AI was developed as part of the Advanced Python course at ECAM. It is designed to play the board game **Quarto** and compete against other student AIs in a tournament hosted on a shared server. The AI is capable of handling multiple games simultaneously and calculating optimal moves in real-time.

For details about the tournament server, visit:  
[PI2C Championship Runner](https://github.com/qlurkin/PI2CChampionshipRunner)

---

## Authors

- [Mathieuxyz](https://github.com/Mathieuxyz)  
- [MastrAmedeo](https://github.com/MastrAmedeo)

---

## Installation

Install the required libraries with:

```bash
python -m pip install -r requirements.txt
```

The used libraries for this project are :
- pytest
- win
- socket
- json
- numpy

## How to run this AI
Go to Socket/server_connector.py and run the script by checking the following information in the "__name__" == main section:

- The information of the initial message : important to indicate what your credentials are and on what port you'll be listening
```shell
message = {"request": "subscribe",
        "port": 4000, #the port
        "name": "Ours polaire", #your name
        "matricules": ["101010", "0101010"] #your student id
        }
```
- The port and host number to connect to the contest server
```shell
client = Client('172.17.10.133', 3000, message)
```

In the end it should look like that :

```shell
if __name__ == "__main__" :
    message = {"request": "subscribe",
            "port": 4000,
            "name": "Tartiflette",
            "matricules": ["23363", "23049"]
            }
    client = Client('172.17.10.133', 3000, message)
    client.subscribe()
```

## The strategy of this AI

In progress, for the moment its random.






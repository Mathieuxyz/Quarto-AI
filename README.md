# Quarto-AI

![Run Tests](https://github.com/Mathieuxyz/Quarto-AI/actions/workflows/test.yml/badge.svg)

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

### 1. Finding a Winning Move

- The AI first checks all available positions on the board.
- For each free spot, it simulates placing the current piece and checks if this leads to an immediate win (four pieces sharing a common characteristic).

Example:
```python
for position in free_positions:
    test_board = copy.deepcopy(self.board)
    test_board[position] = self.piece
    if self.win(test_board):
        return position  # Play here to win immediately
```

- If a winning move is found, the AI plays it instantly.

### 2. Choosing the next piece

- If a winning move is played, the AI randomly selects a piece among those that have not yet been used.

```python
remaining_pieces = self.pieces - self.played
chosen_piece = random.choice(list(remaining_pieces))
```

- If no immediate win is possible, the AI uses a Minimax algorithm (with a depth of 2) to find the best move and select a strategic piece to give the opponent.

Minimax explores all possible placements of the current piece on free positions and simulates handing each remaining piece to the opponent. It alternates turns recursively, maximizing score on the AI's turn and minimizing on the opponent’s turn. Immediate wins are scored ±1000; otherwise, a heuristic evaluates board favorability based on shared features. Search depth is limited to 2 plies to balance performance and strategic foresight. The AI selects the move (position + next piece) that optimizes its outcome assuming perfect opponent play.


## License:

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
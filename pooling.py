import random
lines = [[0, 1, 2, 3],
         [4, 5, 6, 7],
         [8, 9, 10, 11],
         [12, 13, 14, 15],
         [0, 4, 8, 12],
         [1, 5, 9, 13],
         [2, 6, 10, 14],
         [3, 7, 11, 15],
         [0, 5, 10, 15],
         [3, 6, 9, 12]]

pieces = {
    "BDEC",
    "BDEP",
    "BDFC",
    "BDFP",
    "BLEC",
    "BLEP",
    "BLFC",
    "BLFP",
    "SDEC",
    "SDEP",
    "SDFC",
    "SDFP",
    "SLEC",
    "SLEP",
    "SLFP",
    "SLFC"
  }

state = {
  "players": ["LUR", "FKY"],
  "current": 0,
  "board": [
    None,
    "BDEC",
    None,
    "SDFP",
    None,
    None,
    None,
    None,
    None,
    "SLFC",
    None,
    None,
    "BLFP",
    "BLEC",
    None,
    None
  ],
  "piece": "BLEP"
}

def board():

    board = {}
    played = set()
    for i in range(len(state["board"])):
        if state["board"][i] != None:
            board.update({i: state["board"][i]})
            played.add(state["board"][i])
    return board, played

played = board()[1]
board = board()[0]
print(board)

def win(board: dict, lines: list):

    for line in lines:
        familly = ["B", "S", "D", "L", "E", "F", "C", "P"]

        for i in line:
            if i in board:
                familly = list(set(familly).intersection(set(board[i])))
                print(familly)

                if len(familly) == 1:
                    return True
    return False 

def chose_case():
    free = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , 14, 15}
    boardtest = board
    for i in board:
        free = free - {i}

    for i in free:
        boardtest.update({i: state["piece"]})
        if win(boardtest, lines) == True:
            return i
    
    return random.choice(list(free))

def give_piece():
    choices = pieces - played
    return random.choice(list(choices))



print(chose_case())
print(give_piece()) 
import random

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


def give_piece():
    choices = pieces - played
    return random.choice(list(choices))

print(give_piece())
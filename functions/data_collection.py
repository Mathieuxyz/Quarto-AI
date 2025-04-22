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

    for i in range(len(state["board"])):
        if state["board"][i] != None:
            board.update({i: state["board"][i]})
    return board

print(board())
from dataclasses import dataclass
import random
import copy


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


@dataclass
class quartoAI:

    board : dict
    played : set
    lines : list
    free : set
    piece : str
    

    def __init__(self, state):

        self.board = {}
        self.played = set()
        self.lines = [[0, 1, 2, 3],
                [4, 5, 6, 7],
                [8, 9, 10, 11],
                [12, 13, 14, 15],
                [0, 4, 8, 12],
                [1, 5, 9, 13],
                [2, 6, 10, 14],
                [3, 7, 11, 15],
                [0, 5, 10, 15],
                [3, 6, 9, 12]]
        self.free = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , 14, 15}
        self.piece = state["piece"]

        #offload toutes les données liées au board du state (cree un board en sous forme de dictionaire)

        for i in range(len(state["board"])):
            if state["board"][i] != None:
                self.board.update({i: state["board"][i]})
                self.played.add(state["board"][i])

    def win(self, board: dict):

        for line in self.lines:
            family = set("BSDLEFCP")

            for i in line:
                if i in self.board:
                    family &= set(board[i]) 
                    
                    if len(family) == 1:
                        return True
        return False 


    def chose_case(self):
        test_board = copy.deepcopy(self.board)
        occupied = set(self.board.keys())
        free = set(range(16)) - occupied

        for i in free:
            test_board[i] = self.piece
            if self.win(test_board):
                self.board = test_board
                return i

        return random.choice(list(free))
    
    
    
ai = quartoAI(state)
case = ai.chose_case()
print(case)
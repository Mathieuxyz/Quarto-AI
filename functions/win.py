import numpy as np

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

board = {8: "abc", 4: "sjf", 0: "abd"}
played = ["abc", "sjf", "abd"]

def boardupdate(piece: str, pos: int, board: dict, played : tuple):

    if pos not in board and piece not in played:
        board.update({pos: piece})
        played.append(piece)


def win(board: dict, lines: list):

    n = 0

    for j in lines:
        for i in board:
            if i in j:
                n =+ 1
                if n == 3:
                    return "won"


boardupdate("adc", 12, board, played)
print(board)

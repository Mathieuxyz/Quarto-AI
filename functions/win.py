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

board = {8: "BDEC", 4: "BLEC", 0: "BDFC"}
played = {"BDEC", "BLEC", "BDFC"}

def boardupdate(piece: str, pos: int, board: dict, played : tuple):

    if pos not in board and piece not in played:
        board.update({pos: piece})
        played.add(piece)


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


boardupdate("BDEP", 12, board, played)
print(board)
print(win(board, lines))

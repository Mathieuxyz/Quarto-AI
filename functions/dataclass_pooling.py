from dataclasses import dataclass
import random
import copy

@dataclass
class quartoAI:

    board : dict
    played : set
    lines : list
    free : set
    piece : str
    pieces :set
    

    def __init__(self, state): #receiving all the info and transforming it into dictionnaries

        self.board = {} #the actual board
        self.played = set() #the played pieces
        self.lines = [[0, 1, 2, 3],[4, 5, 6, 7],[8, 9, 10, 11],[12, 13, 14, 15],[0, 4, 8, 12],[1, 5, 9, 13],[2, 6, 10, 14],[3, 7, 11, 15],[0, 5, 10, 15],[3, 6, 9, 12]]
        self.free = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13 , 14, 15}
        self.piece = state["piece"]
        self.pieces = {"BDEC","BDEP","BDFC","BDFP","BLEC","BLEP","BLFC","BLFP","SDEC","SDEP","SDFC","SDFP","SLEC","SLEP","SLFP","SLFC"}

        #offload toutes les données liées au board du state (cree un board en sous forme de dictionaire)

        for i in range(len(state["board"])):
            if state["board"][i] != None:
                self.board.update({i: state["board"][i]})
                self.played.add(state["board"][i])

    def win(self, board: dict): #this does not check someone won, but helps to estimate if the AI can win directly by putting one new piece (see chose_case function). Takes the imaginary board as argument

        for line in self.lines:
            family = set("BSDLEFCP") #all possible characteristics, with set() all caractheristics are separated

            for i in line: #looks at every line possible
                if i in board: #check if that line is full op pieces in order to go next
                    family &= set(board[i]) #checks that all values that i take (all pieces of the line) have one thing in common
                    
                    if len(family) >= 1: #if so, the combination is a win. >= because they can have muiltiple characteristics in common
                        return True
        return False 


    def chose_case(self): #to place the given piece

        test_board = copy.deepcopy(self.board) #copies the existing board to make edits on it
        occupied = set(self.board.keys()) #makes a set with existing occupied positions
        free = set(range(16)) - occupied

        for i in free: #tries every position to put the piece in
            test_board[i] = self.piece #put the piece in our imaginary board at a postion 
            if self.win(test_board): #if it works out it returns the position 
                self.board = test_board #make sure the new board is uploaded so that give_piece doesn't make an error
                return i 
            
        c = random.choice(list(free)) #TO Modify !!!! This is not complete
        self.board[c] = self.piece

        return c
    
    def give_piece(self):

        occupied = set(self.board.keys())
        free = set(range(16)) - occupied
        choices = self.pieces - self.played #pieces available to play

        for p in choices:
            safe = True  #the piece to give is safe or not

            for i in free: #checks in all available positions if one of them leads to an easy win
                test_board = copy.deepcopy(self.board)
                test_board[i] = p
                if self.win(test_board):
                    safe = False
                    break #if there's only one winning combination we break the loop to try another piece

            if safe:
                return p #TO Modify !!!! This is not complete
        return random.choice(list(choices)) #if nothing is safe we return smth random, last case
    
    def move(self): #after the class is created, we ask to calculate the next move and piece to give

        move = {"pos": self.chose_case(),
                "piece": self.give_piece()
                }

        return move


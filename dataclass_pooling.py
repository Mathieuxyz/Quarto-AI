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
                    
                    if len(family) >= 1 and all(i in board for i in line): #if so, the combination is a win. >= because they can have muiltiple characteristics in common
                        return True
        return False 

    def evaluate(self, board: dict):

        val = 0  #gives a value based on the state of the game, if it is in our favor or in the opponent's favor

        for line in self.lines:
            line_pieces = [board[i] for i in line if i in board]    #creates a list with all the pieces in a line 
            if len(line_pieces) > 1:    #ignore les lignes ou il n'y a que une piece
                common = set(line_pieces[0])
                for piece in line_pieces[1:]:
                    common &= set(piece)
                    val += len(common)  #gives a value based on the amout of common pionts in a line
        return val
    
    def minimax(self, board, played_pieces, depth, our_turn, current_piece):

        if self.win(board):
            return (-1000 if our_turn else 1000), None
        
        if depth == 0 or len(played_pieces) == 16:
            score = self.evaluate(board)
            return score, None
        
        if our_turn:
            best_score = float("-inf")
        else:
            best_score = float("inf")

        best_move = None

        free_positions = set(range(16)) - set(board.keys())

        remaining_pieces = self.pieces - played_pieces - {current_piece}

        for position in free_positions:
            new_board = board.copy()
            new_board[position] = current_piece

            new_played = played_pieces | {current_piece}

            for next_piece in remaining_pieces:
                future_score, _ = self.minimax(new_board, new_played, depth - 1, not our_turn, next_piece)

                if our_turn:
                    if future_score > best_score:
                        best_score = future_score
                        best_move = (position, next_piece) 

                else:
                    if future_score < best_score:
                        best_score = future_score
                        best_move = (position, next_piece)

        return best_score, best_move

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
    
    def move_no_algorithm(self): #after the class is created, we ask to calculate the next move and piece to give

        move = {"pos": self.chose_case(),
                "piece": self.give_piece()
                }

        return move

    def move_minimax(self):
        
        if self.piece is None:
            return {
        "pos": None,
        "piece": random.choice(list(self.pieces))
        }
    

        score, best_move = self.minimax(self.board, self.played, depth = 2, our_turn = True, current_piece = self.piece)
        
        if best_move is None:   # Fallback on basic strategy 
        
            return self.move_no_algorithm()

        return {
        "pos": best_move[0],
        "piece": best_move[1]
        }
    
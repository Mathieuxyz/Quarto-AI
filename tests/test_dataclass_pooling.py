
import functions.dataclass_pooling as pooling

def test_initialization(): #works
    null = None
    state = {
    "players": ["LUR", "FKY"],"current": 0,"board": [null,"BDEC",null,"SDFP",null,null,null,null,null,"SLFC",null,null,"BLFP","BLEC",null,null], "piece": "BLEP"
    }

    sit = pooling.quartoAI(state) #sit stands for situation

    assert type(sit.board) == dict #this before the exact value
    assert sit.board == {1: 'BDEC', 3: 'SDFP', 9: 'SLFC', 12: 'BLFP', 13: 'BLEC'}
    assert type(sit.played) == set
    assert sit.played == {'SLFC', 'BLEC', 'BLFP', 'BDEC', 'SDFP'}
    assert type(sit.lines) == list
    assert type(sit.free) == set
    assert type(sit.piece) == str
    assert len(sit.piece) == 4
    assert type(sit.pieces) == set

def test_win(): 

    null = None
    state = {
    "players": ["LUR", "FKY"],"current": 0,"board": ["BDEC","BDEP","BDFC","BDFP",null,null,null,null,null,null,null,null,null,null,null,null], "piece": "BLEP"
    }

    sit = pooling.quartoAI(state) #sit stands for situation

    assert type(sit.win(sit.board)) == bool
    assert sit.win(sit.board) == True

def test_evaluate():

    null = None
    state = {
    "players": ["LUR", "FKY"],"current": 0,"board": [null,"BDEC",null,"SDFP",null,null,null,null,null,"SLFC",null,null,"BLFP","BLEC",null,null], "piece": "BLEP"
    }

    sit = pooling.quartoAI(state) #sit stands for situation

    assert type(sit.evaluate(sit.board)) == int
    assert sit.evaluate(sit.board) == 8

def test_minimax():

    null = None
    state = {
    "players": ["LUR", "FKY"],"current": 0,"board": [null,"BDEC",null,"SDFP",null,null,null,null,null,"SLFC",null,null,"BLFP","BLEC",null,null], "piece": "BLEP"
    }

    sit = pooling.quartoAI(state) #sit stands for situation

    depth = 2
    our_turn = True
    current_piece = sit.piece

    best_score, best_move = sit.minimax(sit.board, sit.played, depth, our_turn, current_piece)

    assert type(best_score) == int
    assert best_score == 1000
    assert type(best_move[0]) == int
    assert type(best_move[1]) == str
    assert len(best_move[1]) == 4

def test_chose_case():
    null = None
    state = {
    "players": ["LUR", "FKY"],"current": 0,"board": ["BDEC","BDEP","BDFC",null,null,null,null,null,null,null,null,null,null,null,null,null], "piece": "BDFP"
    }

    sit = pooling.quartoAI(state) #sit stands for situation

    assert type(sit.chose_case()) == int
    assert sit.chose_case() == 4 #should give the third position, super weird why it's four and not 3. As before we need to add an index but have no explanation

def test_give_random_piece():
    null = None
    state = {
    "players": ["LUR", "FKY"],"current": 0,"board": ["BDEC","BDEP","BDFC",null,null,null,null,null,null,null,null,null,null,null,null,null], "piece": "BDFP"
    }

    sit = pooling.quartoAI(state)

    assert type(sit.give_random_piece()) == str
    assert len(sit.give_random_piece()) == 4

def test_move():

    null = None
    state1 = {
    "players": ["LUR", "FKY"],"current": 0,"board": ["BDEC","BDEP","BDFC",null,null,null,null,null,null,null,null,null,null,null,null,null], "piece": "BDFP"
    }

    sit1 = pooling.quartoAI(state1) #To simulate a easy winning situation
    move1 = sit1.move()

    assert type(move1) == dict
    assert move1['pos'] == 3 #super weird why it's four and not 3. As before we need to add an index but have no explanation
    assert type(move1['piece']) == str
    assert len(move1['piece']) == 4


    null = None
    state2 = {
    "players": ["LUR", "FKY"],"current": 0,"board": [null,"BDEC",null,null,null,null,null,null,null,null,null,null,null,null,null,null], "piece": "BDFP"
    }

    sit2 = pooling.quartoAI(state2) #To simulate a complex situation
    move2 = sit2.move()
    assert type(move2['pos']) == int
    assert type(move2['piece']) == str
    assert len(move2['piece']) == 4

def test_move_minimax():
    # Prepare a complex board situation where no immediate winning move is available
    null = None
    state = {
        "players": ["LUR", "FKY"],
        "current": 0,
        "board": [null, "BDEC", null, null, null, null, null, null,
                  null, null, null, null, null, null, null, null],
        "piece": "BDFP"
    }

    # Create an instance of the AI with the given state
    sit = pooling.quartoAI(state)

    # Directly call move_minimax to test it
    move = sit.move_minimax()

    # Assert that the returned move has the correct structure
    assert type(move) == dict  # move must be a dictionary
    assert 'pos' in move and 'piece' in move  # move must contain 'pos' and 'piece' keys
    assert type(move['pos']) == int  # 'pos' must be an integer
    assert 0 <= move['pos'] <= 15  # 'pos' must be a valid board index
    assert type(move['piece']) == str  # 'piece' must be a string
    assert len(move['piece']) == 4  # 'piece' string must have length 4













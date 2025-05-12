import functions.dataclass_pooling as pooling

from unittest.mock import MagicMock

def test_initialization(): #works
    null = None
    state = {
    "players": ["LUR", "FKY"],"current": 0,"board": [null,"BDEC",null,"SDFP",null,null,null,null,null,"SLFC",null,null,"BLFP","BLEC",null,null], "piece": "BLEP"
    }

    sit = pooling.quartoAI(state) #sit stands for situation

    assert type(sit.board) == dict
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

    assert sit.win(sit.board) == True

def test_evaluate():

    null = None
    state = {
    "players": ["LUR", "FKY"],"current": 0,"board": [null,"BDEC",null,"SDFP",null,null,null,null,null,"SLFC",null,null,"BLFP","BLEC",null,null], "piece": "BLEP"
    }

    sit = pooling.quartoAI(state) #sit stands for situation

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

    assert best_score == 1000
    assert type(best_move[0]) == int
    assert len(best_move[1]) == 4
    assert type(best_move[1]) == str

def test_chose_case():
    









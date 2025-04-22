import pytest
import win

def test_duppieces():
    s = {}
    for i in win.board:
        s.add(win.board[i])

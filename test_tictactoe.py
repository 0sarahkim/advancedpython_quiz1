from tictactoe import tictactoe
import numpy as np



def test_o_win_row():
	game1 = np.array([['O','O','O'],['X','X','O'],['X','O','X']])
	assert tictactoe(game1) == 'O win!!!'

def test_o_win_col():
	game11 = np.array([['O','X','O'],['X','X','O'],['X','O','O']])
	assert tictactoe(game11) == 'O win!!!'


def test_x_win_row():
	game2 = np.array([['X','X','X'],['X','O','O'],['O','O','X']])
	assert tictactoe(game2) == 'X win!!!'

def test_x_win_col():
	game22 = np.array([['X','O','X'],['X','O','O'],['X','X','O']])
	assert tictactoe(game22) == 'X win!!!'


def test_incomplete():
	game3 = np.array([['X',' ','X'],[' ',' ','O'],['X','O',' ']])
	assert tictactoe(game3) == 'Game is not completed'


def test_error():
	game4 =np.array([['X','X','X'],['O','O','O'],['X','O','X']])
	assert tictactoe(game4) == 'Result is ambiguous!!!'


def test_x_win_diagonal():
	game5 = np.array([['X','O','O'],['O','X','O'],['O','X','X']])
	assert tictactoe(game5) == 'X win!!!'


def test_o_win_diagonal():
	game5 = np.array([['O','X','X'],['X','O','X'],['X','O','O']])
	assert tictactoe(game5) == 'O win!!!'
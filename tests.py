import pytest
from ttt_oop import *

def test_empty_board():
  playerX = HumanPlayer('X')
  playerO = BotPlayer('O')
  game = Game(playerX, playerO)
  assert game.board.board == [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
  assert game.board.is_full() == False

def test_board_make_move():
  playerX = HumanPlayer('X')
  playerO = BotPlayer('O')
  game = Game(playerX, playerO)
  game.board.make_move(0, 'X')
  assert game.board.board == ['X', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']

def test_check_player_symbol():
  playerX = HumanPlayer('X')
  playerO = BotPlayer('O')
  assert playerX.symbol == 'X'
  assert playerO.symbol == 'O'

def test_switch_player():
  playerX = HumanPlayer('X')
  playerO = BotPlayer('O')
  game = Game(playerX, playerO)
  assert game.current_player == playerX
  game.switch_player()
  assert game.current_player == playerO

def test_game_with_winner():
  playerX = HumanPlayer('X')
  playerO = BotPlayer('O')
  game = Game(playerX, playerO)
  game.board.make_move(0, 'X')
  game.board.make_move(1, 'O')
  game.board.make_move(2, 'X')
  game.board.make_move(3, 'O')
  game.board.make_move(4, 'X')
  game.board.make_move(5, 'O')
  game.board.make_move(6, 'X')
  game.board.make_move(7, 'O')
  game.board.make_move(8, 'X')
  assert game.board.check_winner(playerX.symbol) == True
  assert game.board.check_winner(playerO.symbol) == False
  assert game.board.is_full() == True

def test_game_no_winner():
  playerX = HumanPlayer('X')
  playerO = HumanPlayer('O')
  game = Game(playerX, playerO)
  game.board.make_move(0, 'X')
  game.board.make_move(1, 'O')
  game.board.make_move(2, 'X')
  game.board.make_move(3, 'O')
  game.board.make_move(4, 'X')
  game.board.make_move(5, 'X')
  game.board.make_move(6, 'O')
  game.board.make_move(7, 'X')
  game.board.make_move(8, 'O')
  assert game.board.check_winner(playerX.symbol) == False
  assert game.board.check_winner(playerO.symbol) == False
  assert game.board.is_full() == True

def test_board_valid_move():
  playerX = HumanPlayer('X')
  playerO = HumanPlayer('O')
  game = Game(playerX, playerO)
  game.board.make_move(0, 'X')
  game.board.make_move(1, 'O')
  game.board.make_move(2, 'X')
  assert game.board.is_valid_move(0) == False
  assert game.board.is_valid_move(1) == False
  assert game.board.is_valid_move(3) == True

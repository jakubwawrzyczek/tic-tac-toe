from board import Board
from game_engine import GameEngine
from players import Player

board = Board()
player_x = Player(input('Choose username for "X": '))
player_o = Player(input('Choose username for "O": '))

while True:
    board.set_value(int(input('Choose empty board place: ')), 'x')
    board.print_board()

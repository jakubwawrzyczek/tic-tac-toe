from board import Board
from game_engine import GameEngine
from players import Player

game_engine = GameEngine()
board = Board()
player_x = Player(input('Choose username for "X": '))
player_o = Player(input('Choose username for "O": '))

while True:
    index = input('Index: ')
    value = 'x'
    game_engine.choose_place_on_the_board(index, value, board)
    board.print_board()

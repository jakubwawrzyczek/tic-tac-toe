from board import Board
from game_engine import GameEngine
from players import Player

game_engine = GameEngine()
board = Board()
player_x = Player(input('Choose username for "X": '))
player_o = Player(input('Choose username for "O": '))

while game_engine.is_game_still_on(board):
    index = input('Index: ')

    game_engine.choose_place_on_the_board(index, board)
    game_engine.change_player()

    board.print_board()

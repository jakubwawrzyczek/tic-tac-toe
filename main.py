from board import Board
from game_engine import GameEngine
from players import Player

game_engine = GameEngine()
board = Board()
player_x = Player(input('Choose username for "X": '), 'x')
player_o = Player(input('Choose username for "O": '), 'o')

board.print_instructions()

while game_engine.is_game_still_on(board):
    game_engine.change_player(player_x, player_o)
    index = input('Field Index: ')

    game_engine.choose_field_on_the_board(index, board)

    board.print_board()

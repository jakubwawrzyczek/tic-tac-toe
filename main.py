from board import Board
from game_engine import GameEngine
from players import Player

game_engine = GameEngine()
board = Board()
player_x = Player(input('Choose username for "X": '), 'x')
player_o = Player(input('Choose username for "O": '), 'o')

game_engine.current_player = player_x

while game_engine.is_game_still_on(board):
    index = input('Index: ')

    if game_engine.is_index_ok(index, board):
        game_engine.change_player(player_x, player_o)
        game_engine.choose_place_on_the_board(index, board)

    board.print_board()

class GameEngine:

    def __init__(self):
        self.current_player = 'x'

    def message(self, text):
        print('\n\n---------')
        print(f'\n\n{text}\n\n')
        print('---------')

    def choose_place_on_the_board(self, index, board):
        index = int(index)
        if 0 < index < 10 and board.is_place_empty(index):
            board.set_value(index, self.current_player.value)
        else:
            print('This place is taken, or integer isn\'t between 1 and 9.')

    def change_player(self, player_x, player_o):
        if self.current_player == player_x:
            self.current_player = player_o
        else:
            self.current_player = player_x

    def is_game_still_on(self, board):
        if board.is_full():
            self.message('No more possible choices!')
            return False
        elif board.check_for_win():
            self.message(f'{self.current_player.username} wins!')
            return False
        else:
            return True

    def is_index_ok(self, index, board):
        try:
            int(index)
        except ValueError:
            return False
        else:
            index = int(index)

            if 0 < index < 10 and board.is_place_empty(index):
                return True
            else:
                return False

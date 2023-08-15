class GameEngine:

    def __init__(self):
        self.current_player = 'x'

    def message(self, text):
        print('---------')
        print(f'\n\n{text}\n\n')
        print('---------')

    def choose_place_on_the_board(self, index, board):
        try:
            int(index)
        except ValueError:
            print("Incorrect value. You need to provide integer between 1 and 9")
        else:
            index = int(index)
            if 0 < index < 10 and board.is_place_empty(index):
                board.set_value(index, self.current_player)
            else:
                print('This place is taken, or integer isn\'t between 1 and 9.')

    def change_player(self):
        if self.current_player == 'x':
            self.current_player = 'o'
        else:
            self.current_player = 'x'

    def is_game_still_on(self, board):
        if board.is_full():
            self.message('No more possible choices!')
            return False
        else:
            return True

class GameEngine:
    def choose_place_on_the_board(self, index, value, board):
        try:
            int(index)
        except ValueError:
            print("Incorrect value. You need to provide integer between 1 and 9")
        else:
            index = int(index)
            if 0 < index < 10 and board.is_empty(index):
                board.set_value(index, value)
            else:
                print('This place is taken, or integer isn\'t between 1 and 9.')


class Board:
    def __init__(self):
        self.board_values = [
            [' ', ' ', ' '],
            [' ', ' ', ' '],
            [' ', ' ', ' ']
        ]

    def print_board(self):
        for i in range(0, 3):
            values = self.board_values[i]
            if i != 0:
                print('---------')
            board_row = ''
            for n in range(0, 3):
                if n != 2:
                    board_row += values[n] + ' | '
                else:
                    board_row += values[n]
            print(board_row)

    def set_value(self, index, value):
        a = (index-1)//3
        b = index - 3*a - 1
        self.board_values[a][b] = value

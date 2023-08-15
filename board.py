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

    def print_instructions(self):
        pass

    def set_value(self, index, value):
        a = (index-1)//3
        b = index - 3*a - 1
        self.board_values[a][b] = value

    def is_place_empty(self, index):
        a = (index - 1) // 3
        b = index - 3 * a - 1
        return self.board_values[a][b] == ' '

    def is_full(self):
        is_full = True
        for row in self.board_values:
            if ' ' in row:
                is_full = False
        return is_full

    def check_for_win(self):
        for i in range(0, 3):
            row = self.board_values[i]
            if row[0] == row[1] == row[2] and row[0] != ' ':
                return True
            elif self.board_values[0][i] == self.board_values[1][i] == self.board_values[2][i] and self.board_values[0][i] != ' ':
                return True
        if self.board_values[0][0] == self.board_values[1][1] == self.board_values[2][2] and self.board_values[0][0] != ' ':
            return True
        elif self.board_values[0][2] == self.board_values[1][1] == self.board_values[2][0] and self.board_values[0][2] != ' ':
            return True

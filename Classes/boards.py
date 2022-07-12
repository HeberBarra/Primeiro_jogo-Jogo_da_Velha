class Boards:

    def __init__(self):
        self.table = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def verify_table(self):
        have_numbers = False
        for table_position in range(9):
            if table_position in self.table:
                have_numbers = True

        return have_numbers

    def add_play_on_board(self, position, value):
        self.table[position] = value

    def reset_board(self):
        self.table = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    def print_board(self):
        full_line = f'|{"-" * 7}|{"-" * 7}|{"-" * 7}|'
        line_with_spaces = f'|{" " * 7}|{" " *7 }|{" " * 7}|'
        top_line = f'/{"-" * 23}\\'
        bottom_line = f'\\{"-" * 23}/'

        print(f'{top_line}',
              f'\n{line_with_spaces}',
              f'\n|   {self.table[6]}   |   {self.table[7]}   |   {self.table[8]}   |',
              f'\n{line_with_spaces}',
              f'\n{full_line}',
              f'\n{line_with_spaces}',
              f'\n|   {self.table[3]}   |   {self.table[4]}   |   {self.table[5]}   |',
              f'\n{line_with_spaces}',
              f'\n{full_line}',
              f'\n{line_with_spaces}',
              f'\n|   {self.table[0]}   |   {self.table[1]}   |   {self.table[2]}   |',
              f'\n{line_with_spaces}',
              f'\n{bottom_line}')


import copy


class Blotris():
    def __init__(self, rows, cols):
        if rows < 5 or cols < 5:
            raise ValueError('rows or cols < 5')
        self._board = [[0 for _ in range(cols)] for _ in range(rows)]

    def add(self, shape, row, col):
        if row < 0 or col < 0:
            return False
        board_copy = copy.deepcopy(self._board)
        for row_index, shape_row in enumerate(shape):
            for col_index, shape_col in enumerate(shape_row):
                if shape_col == 1:
                    try:
                        block_pos = board_copy[row + row_index][col +
                                                                col_index]
                    except IndexError:
                        return False
                    if block_pos == 1:
                        return False
                    board_copy[row + row_index][col + col_index] = 1
        self._board = board_copy
        return True

    def update(self):
        empty_row = [0 for _ in range(len(self._board[0]))]
        full_row = [1 for _ in range(len(self._board[0]))]
        count = 0
        try:
            while True:
                self._board.remove(full_row)
                count += 1
        except ValueError:
            for _ in range(count):
                self._board = [empty_row] + self._board

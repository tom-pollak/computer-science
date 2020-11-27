def create_chequerboard(n):
    if n < 2:
        return None
    board = ''
    for i in range(n):
        for j in range(n):
            if (j % 2 == 0 and i % 2 == 0) or ((j + 1) % 2 == 0 and
                                               (i + 1) % 2 == 0):
                board += 'x'
            else:
                board += '-'
        board += '\n'
    return board

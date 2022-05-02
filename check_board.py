#old commit file no longer used in final code from before I knew how to use github but I still want to show my progress

def check_board(board, index, row, col):
    is_valid = True

    for cols in range(9):
        if cols != col and board[row][cols] == index:
            is_valid = False
    for rows in range(9):
        if rows != row and board[rows][col] == index:
            is_valid = False
    frow = row // 3 * 3
    fcol = col // 3 * 3
    for i in range(frow, frow + 3):
        for j in range(fcol, fcol + 3):
            if i == row and j == col:
                continue
            if index == board[i][j]:
                is_valid = False

    return is_valid

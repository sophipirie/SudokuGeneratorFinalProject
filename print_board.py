#old commit file no longer used in final code from before I knew how to use github

def print_board(board):
    print('---------------------------------------')
    for i in range(9):
        for j in range(9):
            if j == 0:
                print('| ', board[i][j], end="   ")
            elif (j - 2) % 3 == 0:
                print(board[i][j], ' |', end="")
            else:
                print(board[i][j], '  ', end="")
        print('')
        if (i - 2) % 3 == 0:
            print('---------------------------------------')

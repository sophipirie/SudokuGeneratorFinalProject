import numpy as np
class BlankBoard:
    def __init__(self):
        self.board = (np.zeros((9, 9))).astype(int)

    def __str__(self):
        m = ''
        m += ('---------------------------------\n')
        for i in range(9):
            for j in range(9):
                if j == 0:
                    if self.board[i, j] != 0:
                        m += f'| {self.board[i, j]} '
                        m.join(m)
                    else:
                        m += f'|   '
                        m.join(m)
                elif (j - 2) % 3 == 0:
                    if self.board[i, j] != 0:
                        m += f' {self.board[i, j]} | '
                        m.join(m)
                    else:
                        m += f'   | '
                        m.join(m)
                else:
                    if self.board[i, j] != 0:
                        m += f' {self.board[i, j]} '
                        m.join(m)
                    else:
                        m += f'   '
                        m.join(m)
            m += ('\n')
            m.join(m)
            if (i - 2) % 3 == 0:
                m += ('---------------------------------\n')
                m.join(m)
        return m
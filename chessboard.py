from distutils import dir_util
import numpy as np

class ChessBoard:
    direction = np.array([[1, 0], [0, 1], [1, 1], [1, -1]])

    def __init__(self):
        self.board = np.full((15, 15), -1)

    def __str__(self):
        ret = '  '
        for i in range(15):
            ret += '%3d' % i
        ret += '\n'
        for i in range(15):
            ret += '%3d' % i + ' '
            for j in range(15):
                if self.board[i, j] == -1:
                    ret += '*  '
                elif self.board[i, j] == 0:
                    ret += 'x  '
                else:
                    ret += 'o  '
            ret += '\n'
        return ret

    def in_bound(x, y) -> bool:
        if (x < 0) | (x > 14) | (y < 0) | (y > 14):
            return False
        return True

    def update(self, x, y, color) -> bool:
        if self.board[x, y] == -1:
            self.board[x, y] = color
            self.latest_x = x
            self.latest_y = y
            return True
        return False
    
    def check_win(self) -> bool:
        pos = np.array([self.latest_x, self.latest_y])

        for i in range(4):
            l, r = 0, 0
            dir = self.direction[i, :]

            while True:
                npos = pos - l * dir
                if ChessBoard.in_bound(npos[0], npos[1]) == False:
                    break
                if self.board[npos[0], npos[1]] != self.board[pos[0], pos[1]]:
                    break
                l += 1
                
            while True:
                npos = pos + r * dir
                if ChessBoard.in_bound(npos[0], npos[1]) == False:
                    break
                if self.board[npos[0], npos[1]] != self.board[pos[0], pos[1]]:
                    break
                r += 1
            if l + r - 1 == 5:
                return True

        return False
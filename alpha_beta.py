from cmath import inf
from email.utils import collapse_rfc2231_value
import numpy as np
from chessboard import ChessBoard

LAYER_THRESH = 2
INF = 1000000

class Alpha_Beta_Tree:
    def __init__(self, board: ChessBoard = None):
        self.board = board
        self.root_color = 1 - board.board[board.latest_x, board.latest_y]

    def calc_val(self, parent_val, sp:bool, dep:int = LAYER_THRESH):
        if dep >= LAYER_THRESH:
            return self.board.getvalue() * (1 - self.root_color*2), self.board.latest_x, self.board.latest_y
        if self.board.check_win():
            if dep & 1:
                return INF, self.board.latest_x, self.board.latest_y
            return -INF, self.board.latest_x, self.board.latest_y

        if dep & 1:
            # parent wants to maximize
            # current wants to minimize
            ret = INF
            for i in range(15):
                for j in range(15):
                    if sp & (5 <= i) & (i <= 9) & (5 <= j) & (j <= 9):
                        continue
                    if (self.board.board[i, j] == -1) & (self.board.cnt_grid[i, j] > 0):
                        lastet_x, lastet_y = self.board.latest_x, self.board.latest_y
                        current_color = 1 - self.board.board[lastet_x, lastet_y]
                        self.board.update(i, j, current_color)
                        temp=self.board.gettemp()
                        child_val, _useless0, _useless1 = self.calc_val(ret, sp, dep + 1)
                        if child_val < ret:
                            ret = child_val
                            ret_x, ret_y = i, j
                            if ret <= parent_val:
                                self.board.backward(lastet_x, lastet_y, temp)
                                return ret, -1, -1

                        self.board.backward(lastet_x, lastet_y, temp)
        else:
            # parent wants to minimize
            # current wants to maximize
            ret = -INF
            for i in range(15):
                for j in range(15):
                    if sp & (5 <= i) & (i <= 9) & (5 <= j) & (j <= 9):
                        continue
                    if (self.board.board[i, j] == -1) & (self.board.cnt_grid[i, j] > 0):
                        lastet_x, lastet_y = self.board.latest_x, self.board.latest_y
                        current_color = 1 - self.board.board[lastet_x, lastet_y]
                        self.board.update(i ,j, current_color)
                        temp=self.board.gettemp()
                        child_val, _useless0, _useless1 = self.calc_val(ret, sp, dep + 1)
                        if child_val > ret:
                            ret = child_val
                            ret_x, ret_y = i, j
                            if ret >= parent_val:
                                self.board.backward(lastet_x, lastet_y, temp)
                                return ret, -1, -1
                        
                        self.board.backward(lastet_x, lastet_y, temp)

        return ret, ret_x, ret_y
    
    def choose(self, sp:bool = False):
        ret, x, y = self.calc_val(2*INF, sp, 0)
        return x, y
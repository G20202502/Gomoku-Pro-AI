from distutils import dir_util
import numpy as np

class ChessBoard:
    direction = np.array([[1, 0], [0, 1], [1, 1], [1, -1]])
    score_list1=[
    (5,(0,1,1,0,0)),
    (5,(0,0,1,1,0)),
    (50,(1,0,1,1,0)),
    (50,(1,1,0,1,0)),
    (50,(0,1,1,1,0)),
    (20,(0,0,1,1,1,2)),
    (20,(2,1,1,1,0,0)),
    (200,(1,1,1,0,1)),
    (200,(1,0,1,1,1)),
    (200,(1,1,0,1,1)),
    (200,(0,1,1,1,1)),
    (200,(1,1,1,1,0)),
    (20000,(1,1,1,1,1)),##this is black
    (-5,(0,2,2,0,0)),
    (-5,(0,0,2,2,0)),
    (-50,(2,0,2,2,0)),
    (-50,(2,2,0,2,0)),
    (-50,(0,2,2,2,0)),
    (-20,(0,0,2,2,2,1)),
    (-20,(1,2,2,2,0,0)),
    (-200,(2,2,2,0,2)),
    (-200,(2,0,2,2,2)),
    (-200,(2,2,0,2,2)),
    (-200,(0,2,2,2,2)),
    (-200,(2,2,2,2,0)),
    (-20000,(2,2,2,2,2))] 
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
    def backward(self, x, y):
        self.board[self.latest_x, self.latest_y] = -1
        self.latest_x = x
        self.latest_y = y   
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
    def cal(self):
        x=self.latest_x
        y=self.latest_y
        temp=self.board[x,y]
        score=0
        for d in range(4):
            dx=self.direction[d,0]
            dy=self.direction[d,1]
            for i in range(0,6):
                position=[]
                for j in range(0,6):
                    newx=x+(j-i)*dx
                    newy=y+(j-i)*dy
                    if (ChessBoard.in_bound(newx,newy)):
                        position.append(self.board[newx,newy]+1)
                    else:
                        break
                    if j==5:
                        pos_5=tuple(k for k in position[0: -1])
                        pos_6=tuple(position)
                        for value,match in self.score_list1:
                            if pos_5==match:
                                score+=value
                            else:
                                if pos_6==match:
                                    score+=value
        self.board[x,y] = -1
        for d in range(4):
            dx=self.direction[d,0]
            dy=self.direction[d,1]
            for i in range(0,6):
                position=[]
                for j in range(0,6):
                    newx=x+(j-i)*dx
                    newy=y+(j-i)*dy
                    if (ChessBoard.in_bound(newx,newy)):
                        position.append(self.board[newx,newy]+1)
                    else:
                        break
                    if j==5:
                        pos_5=tuple(k for k in position[0: -1])
                        pos_6=tuple(position)
                        for value,match in self.score_list1:
                            if pos_5==match:
                                score-=value
                            else:
                                if pos_6==match:
                                    score-=value
        self.board[x,y] = temp  
        return score
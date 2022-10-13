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
        self.current_val=0
        self.temp=0
        self.cnt_grid = np.zeros((15, 15))

    def __str__(self):
        ret = '  '
        for i in range(15):
            ret += '%3d' % i
        ret += '\n'
        for i in range(15):
            ret += '%3d' % i + ' '
            for j in range(15):
                if self.board[i, j] == -1:
                    ret += '·  '
                elif self.board[i, j] == 0:
                    ret += 'X  '
                else:
                    ret += 'O  '
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
            self.temp=self.cal()
            self.current_val+=self.temp

            for d in ChessBoard.direction:
                for i in range(-2, 3):
                   nx = x + i * d[0]
                   ny = y + i * d[1]
                   if ChessBoard.in_bound(nx, ny):
                       self.cnt_grid[nx, ny] += 1

            ##print(self.temp)
            ##print(self.current_val)
            return True
        return False

    def backward(self, x, y, t):
        ##self.temp=self.cal()
        self.board[self.latest_x, self.latest_y] = -1
        for d in ChessBoard.direction:
            for i in range(-2, 3):
                nx = self.latest_x + i * d[0]
                ny = self.latest_y + i * d[1]
                if ChessBoard.in_bound(nx, ny):
                    self.cnt_grid[nx, ny] -= 1
        self.latest_x = x
        self.latest_y = y
        self.current_val-=t

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
        weigh=120-(x-7.5)*(x-7.5)-(y-7.5)*(y-7.5)
        weigh=weigh*(1-2*self.board[x,y])
        ##coe=1-2*self.board[x,y]
        score=weigh                                    
        for d in range(4):
            dx=self.direction[d,0]
            dy=self.direction[d,1]
            for i in range(0,6):
                position=[]
                pos2=[]
                for j in range(0,6):
                    newx=x+(j-i)*dx
                    newy=y+(j-i)*dy
                    if (ChessBoard.in_bound(newx,newy)):
                        position.append(self.board[newx,newy]+1)
                        if (newx,newy) == (x,y):
                            pos2.append(0)
                        else:
                            pos2.append(self.board[newx,newy]+1)
                    else:
                        break
                    if j==5:
                        pos_5=tuple(k for k in position[0: -1])
                        pos_6=tuple(position)
                        pos2_5=tuple(k for k in pos2[0: -1])
                        pos2_6=tuple(pos2)
                        for value,match in self.score_list1:
                            if pos_5==match:
                                score+=value
                            if pos_6==match:
                                score+=value
                            if pos2_5==match:
                                score-=value
                            if pos2_6 == match:
                                score-=value 
        
        return score

    def getvalue(self):
        ##coe=1-2*self.board[self.latest_x,self.latest_y]
        return self.current_val

    def gettemp(self):
        return self.temp
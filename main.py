from alpha_beta import Alpha_Beta_Tree
import simple_gui
import chessboard
import numpy as np
import sys
import os
import time
board = chessboard.ChessBoard()

if __name__ == '__main__':
    AI = simple_gui.Start()
    Round = 0
    ##AItime=0
    while True:
        
        os.system('cls')
        simple_gui.Render_Round(Round, board)
        while True:
            if Round == 0:
                x, y = 7, 7
            elif (Round & 1) == AI:
                ##starttime=time.time()
                tree = Alpha_Beta_Tree(board)
                x, y = tree.choose(sp = (Round == 2))
                ##endtime=time.time()
                ##AItime=-starttime+endtime
            else:
                ##print(AItime)
                x, y = simple_gui.Player_Choose(Round)
            if board.update(x, y, Round & 1) == True:
                break
        if board.check_win():
            simple_gui.Print_Winner(Round)
            exit(0)
        Round += 1
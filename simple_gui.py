import numpy as np
import chessboard
import os

strlist = ['BLACK', 'WHITE']

def Start() -> int:
    print('========WELCOME========')
    while True:
        ret = input('Select your color: black/white:     ')
        if ret[0] == 'b':
            return 0
        elif ret[0] == 'w':
            return 1

def Render_Round(round: int, board) -> None:
    
    print('========', strlist[round&1], '========\n\n')
    print(board, '\n')
    print('=====================')


def Player_Choose():
    while True:
        ret = input('Choose your position, format: x  y:    ')
        ret = ret.split()
        if len(ret) != 2:
            continue
        x = int(ret[0])
        y = int(ret[1])
        if chessboard.ChessBoard.in_bound(x, y):
            break
    return x, y

def Print_Winner(round):
    os.system('cls')
    print('WINNER: ', strlist[round&1])
import numpy as np
import chessboard
import os

strlist = ['BLACK', 'WHITE']

def Start() -> int:
    os.system('cls')
    print('========WELCOME========')
    while True:
        ret = input('Select your color: black/white:     ')
        if ret[0] == 'b':
            return 1
        elif ret[0] == 'w':
            return 0

def Render_Round(round: int, board: chessboard.ChessBoard) -> None:
    
    print('========', strlist[round&1], '========\n\n')
    if round > 0:
        print('Last player choosed: {}  {}.' .format(board.latest_x, board.latest_y))
    print(board, '\n')
    print('=====================')


def Player_Choose(round):
    while True:
        ret = input('Choose your position, format: x  y:    ')
        ret = ret.split()
        if len(ret) != 2:
            continue
        x = int(ret[0])
        y = int(ret[1])
        if chessboard.ChessBoard.in_bound(x, y):
            if (round == 2) & (5 <= x) & (x <= 9) & (5 <= y) & (y <= 9):
                continue
            break
    return x, y

def Print_Winner(round):
    os.system('cls')
    print('WINNER: ', strlist[round&1])
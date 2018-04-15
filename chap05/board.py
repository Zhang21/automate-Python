#!/bin/python3
# coding: utf-8


#棋盘
board = {'左上': ' ', '中上': ' ', '右上': ' ', \
        '左中': ' ', '中中': ' ', '右中': ' ', \
        '左下': ' ', '中下': ' ', '右下': ' '}

def printBoard(board):
    print(board['左上'] + '  |  ' +  board['中上'] + '  |  ' +  board['右上'])
    print('---------------')
    print(board['左中'] + '  |  ' + board['中中'] + '  |  ' + board['右中'])
    print('---------------')
    print(board['左下'] + '  |  ' + board['中下'] + '  |  ' + board['右下'])

turn = 'X'

for i in range(10):
    printBoard(board)
    print('移动 ' + turn + '. 到哪里？')
    print('左/中/右,上/下')
    move = input()
    board[move] = turn

    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(board)

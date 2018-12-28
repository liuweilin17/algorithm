###########################################
# Let's Have Some Fun
# File Name: 794.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Dec 28 16:16:40 2018
###########################################
#coding=utf-8
#!/usr/bin/python

class Solution:
    def validTicTacToe(self, board):
        """
        :type board: List[str]
        :rtype: bool
        """
        row, col = 3, 3
        xNum, oNum = 0, 0 # number of X and O
        for i in range(row):
            for j in range(col):
                if board[i][j] == 'X':
                    xNum += 1
                elif board[i][j] == 'O':
                    oNum += 1
                else: pass

        xWin, oWin = 0, 0 # wether X or O wins
        for i in range(row):
            if board[i][0] == board[i][1] and board[i][1] == board[i][2]:
                xWin = 1 if board[i][0] == 'X' else xWin
                oWin = 1 if board[i][0] == 'O' else oWin

            if board[0][i] == board[1][i] and board[1][i] == board[2][i] and board[0][i] != ' ':
                xWin = 1 if board[0][i] == 'X' else xWin
                oWin = 1 if board[0][i] == 'O' else oWin
        if board[0][0] == board[1][1] and board[1][1] == board[2][2] and board[0][0] != ' ':
            xWin = 1 if board[0][0] == 'X' else xWin
            oWin = 1 if board[0][0] == 'O' else oWin
        if board[0][2] == board[1][1] and board[1][1] == board[2][0] and board[0][2] != ' ':
            xWin = 1 if board[0][2] == 'X' else xWin
            oWin = 1 if board[0][2] == 'O' else oWin

        if oNum > xNum or xNum - oNum > 1: # abnormal number of X and O
            return False
        elif oNum == xNum and xWin: # Last step is O, but X wins already
            return False
        elif oNum == xNum - 1 and oWin: # Last step is X, but O wins already
            return False
        else:
            return True



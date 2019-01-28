###########################################
# Let's Have Some Fun
# File Name: 36.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Jan 27 18:45:54 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#36. Valid Sudoku

class Solution:
    def checkValid(self, lst):
        dt = {}
        for s in lst:
            if s >= '1' and s <= '9':
                if s in dt.keys(): return False
                dt[s] = 1
        return True

    def isValidSudoku1(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # check each row
        for i in range(9):
            if not self.checkValid(board[i]): return False

        # check each column
        for i in range(9):
            if not self.checkValid([line[i] for line in board]): return False

        # check 9 3*3
        for j in [0,3,6]:
            for k in [0,3,6]:
                tmp = []
                for p in range(j,j+3):
                    for q in range(k, k+3):
                        tmp.append(board[p][q])
                        if not self.checkValid(tmp): return False
        return True

    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        row = [{} for i in range(9)] # 9 dict for each row
        col = [{} for i in range(9)] # 9 dict for each column
        box = [{} for i in range(9)] # 9 dict for each box

        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if row[i].get(board[i][j], 0): return False
                    else: row[i][board[i][j]]=1
                    if col[j].get(board[i][j], 0): return False
                    else: col[j][board[i][j]]=1
                    if box[i//3*3+j//3].get(board[i][j], 0): return False # notice!!!
                    else: box[i//3*3+j//3][board[i][j]]=1
        return True

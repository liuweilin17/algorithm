###########################################
# Let's Have Some Fun
# File Name: 130.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri May  3 12:39:15 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#130. Surrounded Regions

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        def explore(i, j, N, M, cnt):
            board[i][j] = cnt
            dr = [1, -1, 0, 0]
            dc = [0, 0, -1, 1]
            for k in range(4):
                r, c = i + dr[k], j + dc[k]
                if 0<=r<N and 0<=c<M and board[r][c] == 'O':
                    explore(r, c, N, M, cnt)

        if not board or not board[0]: return
        N, M = len(board), len(board[0])

        # set all island linking to the border to -1
        for i in range(M):
            if board[0][i] == 'O':
                explore(0, i, N, M, -1)
            if board[N-1][i] == 'O':
                explore(N-1, i, N, M, -1)
        for i in range(N):
            if board[i][0] == 'O':
                explore(i, 0, N, M, -1)
            if board[i][M-1] == 'O':
                explore(i, M-1, N, M, -1)

        # find all island and set it to 'X'
        for i in range(N):
            for j in range(M):
                if board[i][j] == 'O':
                    explore(i, j, N, M, 'X')

        # recover -1
        for i in range(N):
            for j in range(M):
                if board[i][j] == -1:
                    board[i][j] = 'O'

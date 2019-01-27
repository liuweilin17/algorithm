###########################################
# Let's Have Some Fun
# File Name: 289.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Jan 26 12:47:16 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#289. Game of Life

class Solution:
    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        """
        if not board: return

        m = len(board)
        n = len(board[0])

        directions=[(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]

        for i in range(m):
            for j in range(n):
                count = 0
                for p,q in directions:
                    ip, jq = i+p, j+q
                    if ip >=0 and ip < m and jq >= 0 and jq < n:
                        count += board[i+p][j+q]%2
                count += board[i][j] // 2

                board[i][j] = board[i][j] % 2

                if board[i][j] == 1:
                    if count < 2 or count >3:
                        board[i][j] = 0
                        # change the unvisited nodes among neighbors
                        if i+1 < m:
                            board[i+1][j] += 2
                            if j-1 >= 0: board[i+1][j-1] += 2
                            if j+1 < n: board[i+1][j+1] += 2
                        if j+1 < n: board[i][j+1] += 2

                else:
                    if count == 3:
                        board[i][j] = 1
                        # change the unvisited nodes among neighbors
                        if i+1 < m:
                            board[i+1][j] -= 2
                            if j-1 >= 0: board[i+1][j-1] -= 2
                            if j+1 < n: board[i+1][j+1] -= 2
                        if j+1 < n: board[i][j+1] -= 2




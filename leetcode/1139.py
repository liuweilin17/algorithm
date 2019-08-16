###########################################
# Let's Have Some Fun
# File Name: 1139.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun 28 Jul 12:28:51 2019
###########################################
#coding=utf-8
#!/usr/bin/python

class Solution:
    # straightforward method
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        N, M = len(grid), len(grid[0])
        grid1 = [[0] * M for _ in range(N)]
        grid2 = [[0] * M for _ in range(N)]

        for i in range(N):
            pre = 0
            for j in range(M):
                if grid[i][j] == 1 and pre >= 1:
                    grid1[i][j] = pre + 1
                else:
                    grid1[i][j] = grid[i][j]
                pre = grid1[i][j]

        for i in range(M):
            pre = 0
            for j in range(N):
                if grid[j][i] == 1 and pre >= 1:
                    grid2[j][i] = pre + 1
                else:
                    grid2[j][i] = grid[j][i]
                pre = grid2[j][i]

        result = 0
        for i in range(N-1, -1, -1):
            for j in range(M-1, -1, -1):
                cand = min(grid1[i][j], grid2[i][j])
                for k in range(cand-1, -1, -1):
                    # check right_top(i-k,j) and left_bot = (i, j-k)
                    if grid1[i-k][j] >= k+1 and grid2[i][j-k] >= k+1:
                        result = max(result, k+1)


        return result ** 2

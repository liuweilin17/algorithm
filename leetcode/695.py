###########################################
# Let's Have Some Fun
# File Name: 695.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Feb 10 12:29:15 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#695. Max Area of Island

class Solution:
    def maxAreaOfIsland(self, grid: 'List[List[int]]') -> 'int':

        def explore(grid, i, j, m, n):
            grid[i][j] = -1
            ret = 1
            pos = [1, 0, -1, 0, 1]
            for k in range(4):
                p, q = i + pos[k], j+pos[k+1]
                if p < m and p >= 0 and q < n and q >= 0 and grid[p][q] == 1:
                    ret += explore(grid, p, q, m, n)
            return ret

        if not grid or not grid[0]: return 0

        ret = 0
        m, n = len(grid), len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count = explore(grid, i, j, m, n)
                    if count > ret:
                        ret = count

        return ret

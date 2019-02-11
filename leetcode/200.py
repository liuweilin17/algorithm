###########################################
# Let's Have Some Fun
# File Name: 200.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Feb 10 12:20:14 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#200. Number of Islands

class Solution:
    # if the basic iterations do not work, think about dfs!!!
    # simply use the dfs in the map !!!!!!
    def numIslands(self, grid: 'List[List[str]]') -> 'int':
        def explore(grid, i, j, m, n):
            pos = [1,0,-1,0,1]
            grid[i][j] = 'x'
            for k in range(4):
                p = i+pos[k]
                q = j+pos[k+1]
                if p >= 0 and p < m and q >= 0 and q < n \
                and grid[p][q] == '1':
                    explore(grid, p, q, m, n)

        if not grid or not grid[0]: return 0
        m = len(grid)
        n = len(grid[0])
        islands = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    islands += 1
                    explore(grid, i, j, m, n)
        return islands





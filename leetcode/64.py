###########################################
# Let's Have Some Fun
# File Name: 64.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Jan 25 22:46:30 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 64. Minimum Path Sum

class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if i!=0 or j!=0:
                    a = grid[i-1][j] if i-1 >= 0 else float('inf')
                    b = grid[i][j-1] if j-1 >= 0 else float('inf')
                    grid[i][j] += min(a,b)

        return grid[m-1][n-1]

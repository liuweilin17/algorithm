###########################################
# Let's Have Some Fun
# File Name: 63.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Jan 25 22:34:03 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 63. Unique Paths II

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        d = []
        for i in range(m):
            d.append([0]*n)

        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1: # consider special case [[0]]
                    d[i][j] = 0
                else:
                    if i == 0 and j==0: d[i][j] = 1
                    else:
                        a = d[i-1][j] if i-1 >= 0 else 0
                        b = d[i][j-1] if j-1 >= 0 else 0
                        d[i][j] = a+b

        return d[m-1][n-1]


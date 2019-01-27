###########################################
# Let's Have Some Fun
# File Name: 73.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Jan 26 13:36:05 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 73. Set Matrix Zeroes

class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        if not matrix: return

        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    for k in range(m):
                        if matrix[k][j] != 0: matrix[k][j] = 'a'
                    for k in range(n):
                        if matrix[i][k] != 0: matrix[i][k] = 'a'

        for i in range(m):
            for j in range(n):
                matrix[i][j] = 0 if matrix[i][j] == 'a' else matrix[i][j]

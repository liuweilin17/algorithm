###########################################
# Let's Have Some Fun
# File Name: 304.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Sep  4 16:13:01 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#304. Range Sum Query 2D - Immutable

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        N = len(matrix)
        M = len(matrix[0]) if N else 0
        self.sums = [ [0 for _ in range(M+1)] for _ in range(N+1) ]
        for i in range(1, N+1):
            for j in range(1, M+1):
                self.sums[i][j] = self.sums[i-1][j] + self.sums[i][j-1] - \
                 self.sums[i-1][j-1] + matrix[i-1][j-1]

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.sums[row2+1][col2+1] - self.sums[row1][col2+1] -\
    self.sums[row2+1][col1] + self.sums[row1][col1]


# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)

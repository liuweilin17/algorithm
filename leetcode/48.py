###########################################
# Let's Have Some Fun
# File Name: 48.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Jan 24 21:34:17 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 48. Rotate Image
# This is problem related to math, please refer to the evernote of 'rotate matrix'!

class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(i, n - i - 1):
                self.rotateOne(matrix, i, j)

    def rotateOne(self, matrix, start, end):
        n = len(matrix)
        pre = matrix[start][end]
        for i in range(4):
            bak = start
            start = end
            end = n - 1 - bak

            tmp = matrix[start][end]
            matrix[start][end] = pre
            pre = tmp



if __name__ == '__main__':
    s = Solution()
    matrix = [[1,2,3],[4,5,6],[7,8,9]]
    s.rotateOne(matrix, 0, 0)
    print(matrix)

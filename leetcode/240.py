###########################################
# Let's Have Some Fun
# File Name: 240.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Feb  1 01:39:20 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#240. Search a 2D Matrix II

class Solution:
    # O(m+n)
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False

        row = len(matrix)
        col = len(matrix[0])

        # search from the top right corner
        i, j = 0, col-1
        while i < row and j >= 0:
            if matrix[i][j] > target:
                j -= 1
            elif matrix[i][j] < target:
                i += 1
            else:
                return True
        return False

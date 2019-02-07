###########################################
# Let's Have Some Fun
# File Name: 74.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Feb  1 01:38:52 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 74. Search a 2D Matrix

class Solution:
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix: return False

        row = len(matrix)
        col = len(matrix[0])
        left = 0
        right = row*col - 1
        while left <= right:
            mid = (left + right) // 2
            print(matrix[mid//col][mid%col])
            if matrix[mid//col][mid%col] > target:
                right = mid-1
            elif matrix[mid//col][mid%col] < target:
                left = mid+1
            else: return True
        return False


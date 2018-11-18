###########################################
# Let's Have Some Fun
# File Name: 944.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Nov 18 11:06:49 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 944. Delete Columns to Make Sorted

class Solution:
    def minDeletionSize(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        col = len(A[0])
        row = len(A)
        ret = 0
        for i in range(col):
            pre = -1
            for j in range(row):
                if ord(A[j][i]) >= pre:
                    pre = ord(A[j][i])
                else:
                    ret += 1
                    break
        return ret


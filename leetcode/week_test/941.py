###########################################
# Let's Have Some Fun
# File Name: 941.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Nov 18 11:05:12 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 941. Valid Mountain Array
# use flag to record increasing or decreasing
class Solution:
    def validMountainArray(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        l = len(A)
        if l < 3:
            return False
        flag = 1
        for i in range(1,l):
            if flag == 1:
                if A[i] > A[i-1]:
                    continue
                elif A[i] < A[i-1]:
                    if i == 1:
                        return False
                    else:
                        flag = -1
                else:
                    return False
            else:
                if A[i] >= A[i-1]:
                    return False
                else:
                    continue
        if flag == 1:
            return False
        return True

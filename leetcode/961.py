###########################################
# Let's Have Some Fun
# File Name: 961.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Dec 28 21:15:09 2018
###########################################
#coding=utf-8
#!/usr/bin/python
class Solution:
    def repeatedNTimes(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        dt = {}
        l = len(A)
        for i in range(l):
            if A[i] in dt.keys():
                return A[i]
            else:
                dt[A[i]] = 1

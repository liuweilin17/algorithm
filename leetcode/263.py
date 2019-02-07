###########################################
# Let's Have Some Fun
# File Name: 263.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Feb  6 20:47:15 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#263. Ugly Number

class Solution:
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0: return False
        factors = [2,3,5]
        for f in factors:
            while not num % f:
                num //= f
        if num == 1: return True
        else: return False

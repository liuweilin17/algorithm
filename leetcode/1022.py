###########################################
# Let's Have Some Fun
# File Name: 1022.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Mar 24 12:09:07 2019
###########################################
#coding=utf-8
#!/usr/bin/python


# 1022. Smallest Integer Divisible by K
# Given a positive integer K, you need find the smallest positive integer N such that N is divisible by K,
# and N only contains the digit 1.
# Return the length of N.  If there is no such N, return -1.

class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K % 10 not in [1, 3, 7, 9]:
            return -1

        s = set() # Notice, set is necessary, and list could lead to time limit exceed !!!
        t, mod = 0, 0
        for i in range(1, K+1):
            # t = 10 * t + 1
            # mod = t % K
            mod = (10 * mod + 1) % K
            if mod == 0: return i
            if mod in s:
                return -1
            else:
                s.add(mod)

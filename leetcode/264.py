###########################################
# Let's Have Some Fun
# File Name: 264.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Feb  6 21:30:28 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#264. Ugly Number II

class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        t2, t3, t5 = 0, 0, 0
        a = [1] * n
        for i in range(1, n):
            a[i] = min([a[t2]*2, a[t3]*3, a[t5]*5])
            if a[i] == a[t2]*2: t2 += 1
            if a[i] == a[t3]*3: t3 += 1
            if a[i] == a[t5]*5: t5 += 1
        return a[n-1]

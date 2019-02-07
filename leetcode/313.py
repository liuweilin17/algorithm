###########################################
# Let's Have Some Fun
# File Name: 313.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Feb  6 21:36:43 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#313. Super Ugly Number

class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        dt = {}
        for p in primes:
            dt[p] = 0

        d = [1] * n

        for i in range(1, n):
            d[i] = min([d[dt[p]]*p for p in primes])
            for p in primes:
                if d[i] == d[dt[p]]*p: dt[p]+=1

        return d[n-1]

###########################################
# Let's Have Some Fun
# File Name: 279.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Feb  6 19:55:04 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#279. Perfect Squares

import math

class Solution:
    # Time limit exceed
    def numSquares1(self, n):
        """
        :type n: int
        :rtype: int
        """
        # d[i][j]:least sum of square num, i*i: largest square number, j: sum
        # d[i][j] = min(d[t][j-t]+1, d[t'][j])
        d = []
        t = int(math.sqrt(n))+1
        #initialize
        for i in range(t):
            d.append([0] * (n+1))
        for i in range(t):
            d[i][1] = 1
        for i in range(n+1):
            d[1][i] = i

        for i in range(2, t):
            for j in range(2, n+1):
                if j >= i**2:
                    d[i][j] = min(d[i][j-i**2]+1, d[i-1][j])
                else:
                    d[i][j] = d[i-1][j]

        #print(d)
        return d[t-1][n]

    def numSquares2(self, n: 'int') -> 'int':
        int_max = sys.maxsize
        d = [int_max] * (n+1) # d[i] least number of square numbers with sum i
        d[0] = 0
        d[1] = 1
        for i in range(1, n+1):
            j = 1
            while j*j <= i:
                d[i] = min(d[i], d[i-j*j]+1)
                j += 1
        return d[n]


###########################################
# Let's Have Some Fun
# File Name: 96.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Jan 19 17:47:32 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# dynamic programming
class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0

        d = [0] * (n+1) # d[i] is # of unique substrees with i elements
        d[0] = 1
        d[1] = 1
        for i in range(2, n+1):
            for j in range(i):
                d[i] += d[j] * d[i-1-j]
        return d[n]


###########################################
# Let's Have Some Fun
# File Name: 375.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Mar  2 20:59:41 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#375. Guess Number Higher or Lower II

class Solution:
    def getMoneyAmount(self, n: int) -> int:
        # (n+1)*(n+1), dp[i][j], the cost of guessing [i, j]
        dp = []
        for i in range(n+1):
            dp.append([0] * (n+1))
        return self.dp_help(1, n, dp)

    def dp_help(self, begin, end, dp):
        if begin >= end: return 0
        if dp[begin][end] != 0: return dp[begin][end]
        minMax = float('inf')
        for i in range(begin, end):
            maxCost = i + max(self.dp_help(begin, i-1, dp), self.dp_help(i+1, end, dp))
            minMax = min(minMax, maxCost)
        dp[begin][end] = minMax
        return minMax


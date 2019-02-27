###########################################
# Let's Have Some Fun
# File Name: 139.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Feb 26 09:31:50 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#139. Word Break

class Solution:
    # if not using DP, then time limit exceed.
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s) + 1
        dp = [False] * N # dp[i], s[:i] could be word broken
        dp[0] = True
        for i in range(1, N):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i] = True
                    break
        return dp[N-1]


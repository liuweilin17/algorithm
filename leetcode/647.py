###########################################
# Let's Have Some Fun
# File Name: 647.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Apr 26 14:14:10 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 647. Palindromic Substrings 

class Solution:
    def countSubstrings(self, s: str) -> int:
        N = len(s)
        if N == 0: return 0

        # dp[i][j] whether s_i,...,s_j is palindromic
        dp = [N * [0] for i in range(N)]
        for i in range(N-1):
            dp[i][i] = 1
            if s[i] == s[i+1]:
                dp[i][i+1] = 1
        dp[N-1][N-1] = 1

        for i in range(N-3, -1, -1):
            for j in range(i+2, N):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]

        return sum([sum(dp[i]) for i in range(N)])




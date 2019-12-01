###########################################
# Let's Have Some Fun
# File Name: 115.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Oct 15 12:06:50 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#115. Distinct Subsequences

class Solution:
    # top to bottom
    def numDistinct1(self, s: str, t: str) -> int:
        dp = [[-1 for _ in range(len(t)+1)] for _ in range(len(s) + 1)]
        def helper(i, j):
            if dp[i][j] != -1:
                return dp[i][j]
            if len(t) - j > len(s) - i:
                dp[i][j] = 0
                return 0
            elif j >= len(t):
                dp[i][j] = 1
                return 1
            elif i >= len(s):
                dp[i][j] = 0
                return 0
            else:
                if s[i] == t[j]:
                    dp[i][j] = helper(i+1, j+1) + helper(i+1, j)
                    return dp[i][j]
                else:
                    dp[i][j] = helper(i+1, j)
                    return dp[i][j]

        return helper(0, 0)

    # bottom to top
    def numDistinct2(self, s: str, t: str) -> int:
        # dp[i][j] denotes number of t[:j] in s[:i]
        N, M = len(s), len(t)
        if M > N: return 0
        dp = [[0 for _ in range(M+1)] for _ in range(N+1)]
        # if t is empty then, there are one sequence in s
        for i in range(N+1):
            dp[i][0] = 1 
            
        for i in range(1, N+1):
            for j in range(1, M+1):
                if i >= j:
                    if s[i-1] == t[j-1]:
                        dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                    else:
                        dp[i][j] = dp[i-1][j]
        return dp[N][M]

    # with O(M) space
    def numDistinct3(self, s: str, t: str) -> int:
        N, M = len(s), len(t)
        if M > N: return 0
        dp = [0 for _ in range(M+1)] # dp[i] number of subsequence of t[:i]
        dp[0] = 1 # the number of sequence of t[:0] in s[:0]
        for i in range(1, N+1):
            # given s[:i], find the number of subquence of t
            pre = 1 # t[:0] in s[:i-1]
            for j in range(1, M+1):
                tmp = dp[j] # t[:j] in s[:i-1]
                if s[i-1] == t[j-1]:
                    dp[j] = dp[j] + pre # pre is t[:j-1] in s[:i-1]
                pre = tmp
                
        return dp[M]

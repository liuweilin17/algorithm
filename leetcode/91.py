###########################################
# Let's Have Some Fun
# File Name: 91.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri May  3 22:32:15 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#91. Decode Ways

class Solution:
    def numDecodings(self, s: str) -> int:
        N = len(s)
        if N == 0: return 0
        if N == 1 and s[0] != '0': return 1
        if s[0] == '0': return 0

        # dp[i] is the number of ways of decoding from 0 to i.
        # dp[i] = dp[i-1] + dp[i-2]
        dp = [0] * N
        dp[0] = 1
        if s[1] == '0':
            if s[0] == '1' or s[0] == '2':
                dp[1] = 1
            else:
                dp[1] = 0
                return 0
        else:
            if int(s[:2]) <= 26:
                dp[1] = 2
            else:
                dp[1] = 1

        for i in range(2, N):
            if s[i] == '0':
                if s[i-1] == '1' or s[i-1] == '2':
                    dp[i] = dp[i-2]
                else:
                    return 0
            elif s[i-1] == '0':
                dp[i] = dp[i-1]
            else:
                if int(s[i-1:i+1]) <= 26:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]

        return dp[N-1]


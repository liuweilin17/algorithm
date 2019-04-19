###########################################
# Let's Have Some Fun
# File Name: 5.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Apr 19 18:48:09 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#5. Longest Palindromic Substring

class Solution:
    # method 1
    def longestPalindrome1(self, s: str) -> str:
        N = len(s)
        if N <= 1: return s
        maxV = 1
        ret = s[0]
        # initialization
        dp = [[True] * N for i in range(N)]
        for i in range(N-1):
            dp[i][i+1] = (s[i] == s[i+1])
            if dp[i][i+1]:
                ret = s[i:i+2]

        for i in range(N-3, -1, -1):
            for j in range(i+2, N):
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]
                else:
                    dp[i][j] = False

                if dp[i][j] and (j-i+1) > maxV:
                    maxV = j - i + 1
                    ret = s[i:j+1]

        return ret






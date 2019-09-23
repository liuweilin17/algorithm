###########################################
# Let's Have Some Fun
# File Name: 44.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Sep 21 17:08:41 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#44. Wildcard Matching

class Solution:
    def isMatch(self, s: str, p: str) -> bool:


        N, M = len(s), len(p)
        dp = [[0 for i in range(M+1)] for j in range(N+1)] # dp[i][j]
        for i in range(N):
            dp[i][M] = -1
        dp[N][M] = 1
        def helper(s, p, i, j): # if p[j:] matches s[i:]
            if dp[i][j] != 0: return True if dp[i][j] == 1 else False

            N = len(s)
            M = len(p)
            if p[j] == '*':
                # remove consecutive "*"s in p
                for k in range(j+1, M):
                    if p[k] == '*':
                        j = k
                    else:
                        break
                for k in range(i, N+1):
                    if helper(s, p, k, j+1):
                        dp[i][j] = 1
                        return True
                dp[i][j] == -1
                return False
            else:
                if i<N and (s[i] == p[j] or p[j] == '?'):
                    dp[i][j] = 1 if helper(s, p, i+1, j+1) else -1
                    return True if dp[i][j] == 1 else False
                else:
                    dp[i][j] = -1
                    return False

        return helper(s, p, 0, 0)


###########################################
# Let's Have Some Fun
# File Name: 727.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Nov 30 23:14:25 2019
###########################################
#coding=utf-8
#!/usr/bin/python

class Solution:
    # DP
    def minWindow(self, S: str, T: str) -> str:
        # O(M*N), two dimensional dp
        N, M = len(S), len(T)
        # dp[i][j], the first matched index in S[:i] with T[:j]
        dp = [[-1 for _ in range(M+1)] for _ in range(N+1)]
        for i in range(N+1):
            dp[i][0] = i # no matches since T[:0] is empty

        for i in range(1, N+1):
            for j in range(1, M+1):
                if S[i-1] == T[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = dp[i-1][j]
        minL = N+1
        ret = ""
        for i in range(N+1):
            start = dp[i][M]
            if start != -1: # matches
                l = i - start
                if l < minL:
                    minL = l
                    ret = S[start:i]
        return "" if minL == N+1 else ret
    
    # two pointer
    def minWindow(self, S: str, T: str) -> str:
        N, M = len(S), len(T)
        i, j = 0, 0 # s index and t index
        minL = N+1
        while i<N:
            if S[i] == T[j]:
                j += 1
                if j == M: # matches
                    end = i # find ending position
                    # begin match backwards to optimize
                    j = M-1
                    while j >= 0:
                        if S[i] == T[j]:
                            j -= 1
                        i -= 1
                    i += 1 # find starting postion
                    l = end - i + 1
                    if l < minL:
                        ret = S[i:end+1]
                        minL = l
            i += 1
        return "" if minL == N+1 else ret

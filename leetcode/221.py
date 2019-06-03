###########################################
# Let's Have Some Fun
# File Name: 221.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun  2 Jun 11:45:11 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#221. Maximal Square

class Solution:
    # my solution
    def maximalSquare1(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        if N == 0: return 0
        M = len(matrix[0])

        ret = 0
        # dp[i][j] the maximum of length of biggest square ending with (i,j)
        dp = [[0] * M for _ in range(N)]
        for i in range(N):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1: ret = 1
        for i in range(M):
            dp[0][i] = int(matrix[0][i])
            if dp[0][i] == 1: ret = 1

        for i in range(1, N):
            for j in range(1, M):
                dp[i][j] = int(matrix[i][j])
                if matrix[i][j] == '1' and matrix[i-1][j-1] == '1':
                    d = dp[i-1][j-1]
                    for k in range(1, d+1):
                        if matrix[i-k][j] == '1' and matrix[i][j-k] == '1':
                            dp[i][j] += 1
                        else:
                            break
                ret = max(ret, dp[i][j])
        #print(dp)
        return ret * ret
    
    #https://leetcode.com/articles/maximal-square/
    def maximalSquare2(self, matrix: List[List[str]]) -> int:
        N = len(matrix)
        if N == 0: return 0
        M = len(matrix[0])
        
        ret = 0
        # dp[i][j] the maximum of length of biggest square ending with (i-1,j-1)
        # Notice!!!, ending with (i-1, j-1) will much simply code compared with ending with (i, j)
        dp = [[0] * (M+1) for _ in range(N+1)]
            
        for i in range(1, N+1):
            for j in range(1, M+1):
                if matrix[i-1][j-1] == '1':
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                ret = max(ret, dp[i][j])
                
        return ret * ret


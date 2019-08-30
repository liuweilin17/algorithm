###########################################
# Let's Have Some Fun
# File Name: 120.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu 22 Aug 11:16:43 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#120. Triangle

class Solution:
    # top bottom
    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]: return 0
        dp = [] # dp[i][j] the minimum path from top to dp[i][j]
        D = len(triangle)
        for i in range(D):
            dp.append([float('inf') for _ in range(i+1)])
        dp[0][0] = triangle[0][0]

        for i in range(1, D):
            for j in range(i+1):
                if j > 0:
                    dp[i][j] = dp[i-1][j-1] + triangle[i][j]
                if j < i:
                    dp[i][j] = min(dp[i-1][j] + triangle[i][j], dp[i][j])
        # print(dp)
        return min(dp[D-1])

    # bottom top 
    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        if not triangle or not triangle[0]: return 0
        ret = triangle[-1]
        D = len(triangle)
        for i in range(D-2, -1, -1):
            for j in range(i+1):
                ret[j] = min(ret[j], ret[j+1]) + triangle[i][j]
        
        return ret[0]


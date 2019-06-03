###########################################
# Let's Have Some Fun
# File Name: 416.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu 30 May 21:13:25 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#416. Partition Equal Subset Sum

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        if N == 0 or N == 1: return False

        sumV = sum(nums)
        if sumV % 2 != 0:
            return False
        half = sumV // 2

        # 0/1 knapsack problem
        # dp[i][j] whether is possible to have 0,...,i number with subsum as j
        dp = [[False] * (half+1) for i in range(N)]
        if nums[0] <= half:
            dp[0][nums[0]] = True

        for i in range(1, N):
            for j in range(1, half+1):
                if j > nums[i]:
                    dp[i][j] = dp[i-1][j] or dp[i-1][j-nums[i]]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[N-1][half]



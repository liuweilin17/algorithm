###########################################
# Let's Have Some Fun
# File Name: 494.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon May 20 09:52:10 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#494. Target Sum

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums: return 0
        N = len(nums)
        sumV = sum(nums)
        if S > sumV or S < -sumV: return 0

        # dp[i][j], ways of assign symbols on 0,...,i with sum = j - sumV
        dp = [(2 * sumV + 1) * [0] for i in range(N)]
        # print(dp)
        dp[0][nums[0] + sumV] += 1
        dp[0][-nums[0] + sumV] += 1
        for i in range(1, N):
            for j in range(2*sumV + 1):
                if j - nums[i] >= 0:
                    dp[i][j] += dp[i-1][j-nums[i]]
                if j + nums[i] <= 2 * sumV:
                    dp[i][j] += dp[i-1][j+nums[i]]

        return dp[N-1][S + sumV]


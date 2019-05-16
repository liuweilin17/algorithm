###########################################
# Let's Have Some Fun
# File Name: 213.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed 15 May 10:45:32 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 213. House Robber II

class Solution:
    def rob(self, nums: List[int]) -> int:
        N = len(nums)
        if not N: return 0
        if N == 1: return nums[0]
        if N == 2: return max(nums[0], nums[1])
        if N == 3: return max(nums) # Notice

        # rob nums[0] ... nums[N-2]
        dp = [0] * (N-1)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, N-1):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])

        # rob nums[1] ... nums[N-1]
        dpp = [0] * N
        dpp[1] = nums[1]
        dpp[2] = max(nums[1], nums[2])
        for i in range(3, N):
            dpp[i] = max(dpp[i-1], dpp[i-2] + nums[i])

        return max(dp[N-2], dpp[N-1])




###########################################
# Let's Have Some Fun
# File Name: 152.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Mar 29 12:33:33 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#152. Maximum Product Subarray

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # dp1[i], the biggest positive product ending at i
        # dp2[i], the smallest negative product ending at i
        N = len(nums)
        if not N: return 0
        dp1 = [-1] * N
        dp2 = [1] * N
        dp1[0], dp2[0] = nums[0], nums[0]
        for i in range(1, N):
            if nums[i] > 0:
                # dp1[i-1] could be negative, so we need to use max
                dp1[i] = max(nums[i], dp1[i-1]*nums[i])
                # dp2[i-1] could be positive, but will not affect min(dp2)
                dp2[i] = dp2[i-1]*nums[i]
            elif nums[i] < 0:
                # dp2[i-1] could be postive, but will not affect max(dp1)
                dp1[i] = dp2[i-1]*nums[i]
                # dp1[i-1] could be negative, so we need to use min
                dp2[i] = min(dp1[i-1]*nums[i], nums[i])
            else:
                dp1[i], dp2[i] = 0, 0

        return max(dp1)


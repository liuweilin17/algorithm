###########################################
# Let's Have Some Fun
# File Name: 209.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu 29 Aug 12:28:31 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 209. Minimum Size Subarray Sum

class Solution:
    # my method, O(n^2), time limit exceed
    def minSubArrayLen1(self, s: int, nums: List[int]) -> int:
        N = len(nums)
        dt = {0: 0}  # length: sum
        cum_sum = 0
        min_l = N+1
        for i in range(N):
            l = i+1
            cum_sum += nums[i]
            dt[l] = cum_sum
            if cum_sum >= s:
                for j in range(1, min(min_l, l+1)):
                    if cum_sum - dt[l-j] >= s:
                        min_l = j
                        break

        return min_l if min_l != N+1 else 0
    
    # method in Solutions, O(n^2), time limit exceed still
    def minSubArrayLen2(self, s: int, nums: List[int]) -> int:
        N = len(nums)
        sums = [0] * (N+1) # sums[i], the sum of 0, ..., i-1
        for i in range(1, N+1):
            sums[i] = sums[i-1] + nums[i-1]

        t = 0
        min_v = N+1
        for i in range(1, N+1):
            for j in range(i, N+1):
                t = sums[j] - sums[i] + nums[i-1]
                if t >= s:
                    min_v = min(min_v, j-i+1)

        return min_v if min_v != N+1 else 0
   
   # O(n)
    def minSubArrayLen(self, s: int, nums: List[int]) -> int:
        N = len(nums)
        t = 0
        left = 0
        min_v = N+1
        for i in range(N):
            t += nums[i]
            while t >= s:
                min_v = min(min_v, i-left+1)
                t -= nums[left]
                left += 1

        return min_v if min_v != N+1 else 0

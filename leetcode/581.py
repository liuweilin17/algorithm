###########################################
# Let's Have Some Fun
# File Name: 581.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue 14 May 09:49:24 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#581. Shortest Unsorted Continuous Subarray

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        N = len(nums)
        if not N: return 0

        nums_sorted = sorted(nums)
        begin = 0
        for i in range(N):
            if nums[i] == nums_sorted[i]:
                begin += 1
            else: break

        end = N - 1
        for i in range(N-1, -1, -1):
            if end <= begin: return 0
            elif nums[i] == nums_sorted[i]:
                end -= 1
            else: break

        return end - begin + 1

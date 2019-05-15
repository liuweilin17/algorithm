###########################################
# Let's Have Some Fun
# File Name: 448.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon 13 May 13:26:40 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#448. Find All Numbers Disappeared in an Array

class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        N = len(nums)
        for i in range(N):
            n = abs(nums[i]) - 1
            nums[n] = - abs(nums[n])

        # if nums[i] > 0, then i+1 does not exist
        return [i+1 for i in range(N) if nums[i] > 0]



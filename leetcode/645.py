###########################################
# Let's Have Some Fun
# File Name: 645.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 22 14:33:40 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 645. Set Mismatch

class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        if n <= 1: return [0,0]
        duplicate = 0
        pre = 0
        nums.sort()
        for i in range(n):
            if pre and pre == nums[i]:
                duplicate = pre
            pre = nums[i]

        return [duplicate, (1+n)*n//2 - sum(nums) + duplicate]

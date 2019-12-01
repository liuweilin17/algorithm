###########################################
# Let's Have Some Fun
# File Name: 487.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Dec  1 12:36:26 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 487. Max Consecutive Ones II.

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # flip at most one 0
        last = -1 # last position of flipping 0
        left, right = -1, 0
        maxL, tmp = 0, 0
        N = len(nums)
        while left <= right and right < N:
            if nums[right] == 1:
                if left == -1: # find the beginning
                    left = right
                right += 1
            else:
                if last == -1: # we can flip
                    if left == -1: # find the beginning
                        left = right
                    last = right # flip pos is assigned to last
                    right += 1
                else:
                    maxL = max(maxL, right-left)
                    left, right = -1, last+1 # start from last+1
                    last = -1
        if left != -1: # consecutiveOnes has been found
            maxL = max(maxL, right -left)
        return maxL


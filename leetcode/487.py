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
   def findMaxConsecutiveOnes1(self, nums: List[int]) -> int:
        # flip at most one 0
        last = -1 # last position of flipping 0
        left, right = -1, 0
        maxL, tmp = 0, 0
        N = len(nums)
        while left <= right and right < N:
            if nums[right] == 1:
                if left == -1: # find the beginning
                    left = right
            else:
                if last == -1: # we can flip
                    if left == -1: # find the beginning
                        left = right
                    last = right # flip pos is assigned to last
                else:
                    maxL = max(maxL, right-left)
                    left = last + 1
                    last = right
            right += 1
        
        maxL = max(maxL, right -left)
        return maxL

    # follow up question
    def findMaxConsecutiveOnes2(self, nums: List[int]) -> int:
        # follow up question
        ret = 0
        cnt = 0 # number of consecutive ones so far
        pre = -1 # number of consecutive ones before last 0
        for num in nums:
            if num == 1:
                cnt += 1
                ret = max(ret, cnt+pre+1) # last 0 could be flipped, so we add 1
            else:
                ret = max(ret, cnt+1) # current 0 could be flipped, so we add 1
                pre = cnt # number of 1s before current 0 update
                cnt = 0 # number of 1s so far is set to 0
        return ret

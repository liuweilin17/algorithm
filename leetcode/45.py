###########################################
# Let's Have Some Fun
# File Name: 45.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Sep 21 18:41:14 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#45. Jump Game II

class Solution:
    def jump(self, nums: List[int]) -> int:
        N = len(nums)
        step = 0 # number of jump
        farthest_dist = 0 # the farthest distance with #step of jumps
        tmp = 0 # current farthest_dist
        for i in range(N):
            if tmp >= N-1:
                break
            if i > farthest_dist:
                step += 1
                farthest_dist = tmp
            if nums[i] + i > tmp: # Notice this if should be after the last if
                tmp = nums[i] + i
            else: pass

        return step + 1 if tmp != 0 else 0


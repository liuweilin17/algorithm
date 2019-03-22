###########################################
# Let's Have Some Fun
# File Name: 55.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Mar 21 15:27:50 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#55. Jump Game

class Solution:
    def canJump1(self, nums: List[int]) -> bool:
        N = len(nums)
        if not N: return False

        maxPos = 0 # farthest postion it can reach
        for i in range(N):
            if maxPos >= N-1: return True
            maxPos = max(maxPos, i + nums[i])
            if maxPos == i: return False

        return True

    # O(n^2) method will show time limit exceed. It seems only O(n) method could pass the test cases


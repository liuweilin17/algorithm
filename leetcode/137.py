###########################################
# Let's Have Some Fun
# File Name: 137.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 22 18:44:29 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 137. Single Number II
# This is the generalization of one number m duplications, with the all the other numbers k duplicates
# See the solution: 
# 1. https://leetcode.com/problems/single-number-ii/discuss/43295/Detailed-explanation-and-generalization-of-the-bitwise-operation-method-for-single-numbers
# 2. http://liadbiz.github.io/leetcode-single-number-problems-summary/

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # k = 3, p = 1
        x1 = 0
        x2 = 0
        mask = 0
        for i in nums:
            x2 ^= x1 & i
            x1 ^= i
            mask = ~(x1 & x2)
            x2 &= mask
            x1 &= mask
        return x1|x2


###########################################
# Let's Have Some Fun
# File Name: 268.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Oct 30 11:35:53 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 268. Missing Number

class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        sumTrue = (1+l)*l*0.5
        sumV = 0
        for n in nums:
            sumV += n
        return int(sumTrue - sumV)

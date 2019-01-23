###########################################
# Let's Have Some Fun
# File Name: 260.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 22 22:34:46 2019
###########################################
#coding=utf-8
#!/usr/bin/python

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # divide nums into two arrays, each of which contains one unique element

        # find the different bit of the two number
        XOR = 0
        for n in nums:
            XOR ^= n

        mask = 1
        while not XOR & mask:
            mask <<= 1

        # split the nums by using mask
        a, b = 0,0
        for n in nums:
            if n & mask:
                a ^= n
            else:
                b ^= n

        return [a, b]

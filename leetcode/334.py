###########################################
# Let's Have Some Fun
# File Name: 334.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Feb 11 16:26:03 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#334. Increasing Triplet Subsequence

class Solution:
    def increasingTriplet(self, nums: 'List[int]') -> 'bool':
        # use O(nlogn) method of LIS
        l = len(nums)
        if l < 3: return False

        d = [None] * 3
        for n in nums:
            if d[0] == None or n <= d[0]:
                d[0] = n
            elif d[1] == None or n <= d[1]:
                d[1] = n
            else:
                return True

        return False

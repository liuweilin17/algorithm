###########################################
# Let's Have Some Fun
# File Name: 217.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Oct 19 00:59:52 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 217. Contains Duplicate

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_new = list(set(nums))
        if len(nums_new) == len(nums):
            return False
        return True

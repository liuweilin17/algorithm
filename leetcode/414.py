###########################################
# Let's Have Some Fun
# File Name: 414.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Jan 25 21:04:50 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#414. Third Maximum Number

class Solution:
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums = list(set(nums))
        n = len(nums)
        if n < 3: return max(nums)
        arr = [nums[0], nums[1], nums[2]]
        arr.sort()

        for i in range(3, n):
            if nums[i] > arr[0]:
                arr[0] = nums[i]
                arr.sort()

        return arr[0]



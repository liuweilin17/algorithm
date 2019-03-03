###########################################
# Let's Have Some Fun
# File Name: 35.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Mar  2 21:14:16 2019
###########################################
#coding=utf-8
#!/usr/bin/python

class Solution:
    # binary search
    def searchInsert(self, nums: List[int], target: int) -> int:
        N = len(nums)
        low, high = 0, N-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < target:
                low = mid + 1
            elif nums[mid] > target:
                high = mid - 1
            else:
                return mid

        return  low
        # 1. nums[low] = nums[high] = nums[mid] < target, then
        # low = mid + 1, is just the postion of insersion, including
        # inserting a biggest number.
        # 2. nums[low] = nums[high] = nums[mid] > target, then
        # high = mid - 1, mid and low are the just the postion of insertion, including
        # inserting a smallest number

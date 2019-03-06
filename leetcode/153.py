###########################################
# Let's Have Some Fun
# File Name: 153.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Mar  5 21:58:59 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#153. Find Minimum in Rotated Sorted Array

class Solution:
    # method1, is not same as the version of BS I am used to.
    # let's see method2 in the following.
    def findMin1(self, nums: List[int]) -> int:
        N = len(nums)
        low, high = 0, N-1
        if nums[high] > nums[low]:
            return nums[0]
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        return nums[low]
    
    def findMin(self, nums: List[int]) -> int:
        N = len(nums)
        if N == 1: return nums[0] # this is necessary, otherwise it will be out of index in line 12
        low, high = 0, N-1
        if nums[high] > nums[low]:
            return nums[0]
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] < nums[mid-1]:
                return nums[mid]
            if nums[mid+1] < nums[mid]:
                return nums[mid+1]
            if nums[mid] > nums[low]:
                low = mid + 1
            else:
                high = mid - 1

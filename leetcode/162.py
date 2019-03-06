###########################################
# Let's Have Some Fun
# File Name: 162.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 29 17:25:51 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#162. Find Peak Element

class Solution:
    #brutal method
    def findPeakElement1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        for i in range(n):
            pre = nums[i-1] if i-1 >=0 else float('-inf')
            post = nums[i+1] if i+1 < n else float('-inf')
            if nums[i] > pre and nums[i] > post: return i

    #recursive binary search
    def findPeakElement2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        def search(nums,l,r):
            if l == r: return l
            
            mid = (l+r) // 2
            if nums[mid] < nums[mid+1]:
                return search(nums, mid+1, r)
            else:
                return search(nums, l, mid)
            
        n = len(nums)
        return search(nums, 0, n-1) 
    
    #iterative binary search
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        l, r = 0, n-1
        while l<r:
            mid = (l+r)//2
            if nums[mid] < nums[mid+1]:
                l = mid+1
            else:
                r = mid
        return l

    # another iterative binary search
    def findPeakElement(self, nums: List[int]) -> int:
        N = len(nums)
        if N <= 1: return 0
        if nums[0] > nums[1]: return 0
        if nums[-1] > nums[-2]: return N-1

        low, high = 0, N-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid]>nums[mid-1] and nums[mid]>nums[mid+1]:
                return mid
            elif nums[mid] < nums[mid-1]:
                high = mid-1
            else:
                low = mid+1

###########################################
# Let's Have Some Fun
# File Name: 852.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 29 16:25:18 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 852. Peak Index in a Mountain Array

class Solution:
    # brutal method
    def peakIndexInMountainArray1(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        for i in range(1, n-1):
            if A[i] > A[i+1]: return i

    # binary search
    # in binary search, the comparison is not necessarily between low, mid and high !!!
    # in the same time, the initialization, update low, high and the return value is hard for me
    # right now!!! I am going to do 'Binary search' in 'Explore' parts of leetcode!!!
    def peakIndexInMountainArray2(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        n = len(A)
        low, high = 0, n-1
        while low < high:
            mid = (low + high) // 2
            if A[mid] < A[mid+1]:
                low = mid+1
            else:
                high = mid
        return (low + high) // 2 # or low

    def peakIndexInMountainArray3(self, A: List[int]) -> int:
        N = len(A)
        low, high = 0, N-1
        while low <= high:
            mid = (low + high) // 2
            if A[mid] > A[mid-1] and A[mid] > A[mid+1]:
                return mid
            elif A[mid] < A[mid - 1]:
                high = mid - 1
            else:
                low = mid + 1


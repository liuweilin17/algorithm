###########################################
# Let's Have Some Fun
# File Name: 300.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Feb  8 14:54:52 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#300. Longest Increasing Subsequence

class Solution:
    # O(N^2) time, O(N) space
    def lengthOfLIS1(self, nums: List[int]) -> int:
        if not nums: return 0
        # dp[i] the length of LIS ending at i
        N = len(nums)
        dp = [1] * N
        for i in range(1, N):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)
        return max(dp)

    # O(NlogN) time, O(N) space
     def lengthOfLIS2(self, nums: List[int]) -> int:
        if not nums: return 0
        arr = []
        for num in nums:
            ind = self.findInsertPos(arr, num)
            if ind == len(arr):
                arr.append(num)
            else:
                arr[ind] = num
        return len(arr)

    def findInsertPos(self, arr, val):
        if not arr:
            return 0
        # binary search
        N = len(arr)
        left, right = 0, N-1
        while left <= right:
            mid = left + (right-left)//2
            if arr[mid] > val:
                right = mid - 1
            elif arr[mid] < val:
                left = mid + 1
            else:
                return mid
        return left



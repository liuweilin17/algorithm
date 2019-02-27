###########################################
# Let's Have Some Fun
# File Name: 34.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Feb 26 16:49:08 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#34. Find First and Last Position of Element in Sorted Array

class Solution:
    def searchRange1(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)

        low, high = 0, N-1
        pos = -1
        while low <= high:
            mid = (low + high) // 2
            if target == nums[mid]:
                pos = mid
                break
            elif target < nums[mid]:
                high = mid - 1
            else:
                low = mid + 1

        if pos == -1:
            return [-1, -1]
        else:
            start, end = pos, pos
            for i in range(pos, N):
                if nums[i] != target: break
            if nums[i] != target:
                end = i-1
            else:
                end = i
            for i in range(pos, -1, -1):
                if nums[i] != target: break
            if nums[i] != target:
                start = i+1
            else:
                start = i
            return [start, end]

    def searchRang2(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)

        # find the leftmost
        low, high = 0, N
        while low < high:
            mid = (low + high) // 2
            if target <= nums[mid]:
                high = mid
            else:
                low = mid + 1
        if low == N or nums[low] != target:
            return [-1, -1]
        left = low

        # find the rightmost
        low, high = 0, N
        while low < high:
            mid = (low + high) // 2
            if target < nums[mid]:
                high = mid
            else:
                low = mid + 1
        return [left, low-1]

    def searchRange3(self, nums: List[int], target: int) -> List[int]:
        N = len(nums)
        
        # find the leftmost 
        low, high = 0, N-1
        while low <= high:
            mid = (low + high) // 2
            if target <= nums[mid]: 
                # when target is found here, high will stay the same, because mid will be smaller than
                # target from now on.
                # And the while terminates when low is equal to 'mid' which is equal to target.
                high = mid - 1
            else:
                low = mid + 1
        
        if low < N and nums[low] == target:
            left = low
        else:
            return [-1, -1]
        
        # find the rightmost
        low, high = 0, N-1
        while low <= high:
            mid = (low + high) // 2
            if target < nums[mid]:
                high = mid - 1
            else:
                # when target is found here, low will stay the same, because mid will be bigger than
                # target from now on.
                # And the while terminate when high is equal to 'mid' which is equal to target.
                low = mid + 1
        return [left, high]

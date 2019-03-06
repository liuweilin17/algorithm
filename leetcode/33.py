###########################################
# Let's Have Some Fun
# File Name: 33.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Mar  5 17:38:16 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#33. Search in Rotated Sorted Array

class Solution:
    # without finding the pivot
    def search1(self, nums: List[int], target: int) -> int:
        N = len(nums)
        low, high = 0, N-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target: return mid

            if nums[mid] >= nums[low]: # left is in order, '>=' instead of '>'
                if target >= nums[low] and target < nums[mid]:
                    high = mid-1
                else:
                    low = mid+1
            else: # right is in order
                if target > nums[mid] and target <= nums[high]:
                    low = mid+1
                else:
                    high = mid-1
        return -1

    def search2(self, nums: List[int], target: int) -> int:
        N = len(nums)
        
        # finding the pivot
        # must use BS-method2. method1 always fail !!!
        low, high = 0, N-1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid+1
            else:
                high = mid
                
        mov = low
        print(mov)
        low, high = 0, N-1
        while low <= high:
            mid = (low + high) // 2
            real_mid = (mid + mov) % N
            if nums[real_mid] == target: return real_mid
            elif nums[real_mid] > target:
                high = mid-1
            else:
                low = mid+1
        return -1

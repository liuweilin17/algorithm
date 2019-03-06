###########################################
# Let's Have Some Fun
# File Name: 81.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Mar  5 21:19:57 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#81. Search in Rotated Sorted Array II

class Solution:
    # O(n) to remote the duplicates, not good enough
    def search1(self, nums: List[int], target: int) -> bool:
        nums = list(set(nums))
        N = len(nums)
        # find pivot
        low, high = 0, N-1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid

        mov = low
        low, high = 0, N-1
        while low <= high:
            mid = (low + high) // 2
            real_mid = (mid + mov) % N
            if nums[real_mid] == target: return True
            elif nums[real_mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def search2(self, nums: List[int], target: int) -> bool:
        N = len(nums)
        low, high = 0, N-1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target: return True
            
            # notice !!!
            # in this case, we cannot decide which side is in ascending order
            if nums[mid] == nums[low] and nums[mid] == nums[high]:
                low += 1
                high -= 1
                
            elif nums[mid] >= nums[low]:
                if target >= nums[low] and target < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if target > nums[mid] and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
                    
        return False
         


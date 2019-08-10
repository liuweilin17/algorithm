###########################################
# Let's Have Some Fun
# File Name: 27.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon  8 Jul 10:18:44 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#27. Remove Element

class Solution:
    # method 1
    def removeElement1(self, nums: List[int], val: int) -> int:
        i = 0 # the last pos+1 which is not equal to val
        if val not in nums: return len(nums)
        for j in range(len(nums)):
            if nums[j] != val:
                nums[i] = nums[j]
                i += 1
        # nums = nums[:i]
        return i

    # method 2
    def removeElement2(self, nums: List[int], val: int) -> int:
        i = 0
        N = len(nums)
        while i < N:
            if nums[i] == val:
                nums[i] = nums[N-1]
                N -= 1
            else:
                i += 1

        return N



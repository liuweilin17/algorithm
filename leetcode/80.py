###########################################
# Let's Have Some Fun
# File Name: 80.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue  9 Jul 15:45:10 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#80. Remove Duplicates from Sorted Array II

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0 # the last position of no over 2 duplicate num
        c = 0 # the number of appearance
        for j in range(1, len(nums)):
            if nums[j] == nums[i]:
                if c == 1: continue
                else:
                    i += 1
                    nums[i] = nums[j]
                    c = 1
            else:
                i += 1
                nums[i] = nums[j]
                c = 0

        return i+1


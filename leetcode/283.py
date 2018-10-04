###########################################
# Let's Have Some Fun
# File Name: 283.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Oct  4 12:55:34 2018
# 283. Move Zeroes
###########################################
#coding=utf-8
#!/usr/bin/python

class Solution(object):
    # This is just like the partition function in QuickSort!!!!!!!!!!
    # And the Quicksort was learned in the Algorithm
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = -1
        l = len(nums)
        for j in range(l):
            if nums[j] != 0:
                i += 1
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp

if __name__ == '__main__':
    s = Solution()
    nums = [0,1,0,3,12]
    print nums
    s.moveZeroes(nums)
    print nums


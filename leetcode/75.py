###########################################
# Let's Have Some Fun
# File Name: 75.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Jan 28 18:54:35 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#75. Sort Colors

class Solution:
    # my solution, two times of iterations, redundant
    def sortColors1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        # move 0 to the left
        i = -1
        for j in range(n):
            if nums[j] == 0:
                i += 1
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp
        for j in range(i + 1, n):
            if nums[j] == 1:
                i += 1
                tmp = nums[i]
                nums[i] = nums[j]
                nums[j] = tmp

    # Dutch national flag problem,
    # O(n)
    def sortColors2(self, nums):
        n = len(nums)
        # Dutch national flag problem
        red, white = 0, 0
        blue = n - 1
        while white <= blue:
            if nums[white] == 0:
                nums[white], nums[red] = nums[red], nums[white]
                red += 1
                white += 1
            elif nums[white] == 2:
                nums[white], nums[blue] = nums[blue], nums[white]
                blue -= 1
                # no 'white += 1', because nums[blue] is not necessarily '1'
            else:
                white += 1


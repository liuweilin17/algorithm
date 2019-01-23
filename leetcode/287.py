###########################################
# Let's Have Some Fun
# File Name: 287.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 22 13:22:31 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 287. Find the Duplicate Number
# we use Floyd's Tortoise and Hare (Cycle Detection) to detect
# see reference
# https://cs.stackexchange.com/questions/10360/floyds-cycle-detection-algorithm-determining-the-starting-point-of-cycle


class Solution:
    # We could apply Floyd's Tortoise and Hare algorithm on the array.
    # We could tansfer the nums to a linkedlist as follows:
    # nd.val = nums[i]
    # nd.next = nums[nd.val] = nums[nums[i]]
    # since n+1 elements, with each in [1,n], nums[i] will not exceed the index of nums,
    # and if there exists one duplicate in the array, the new linkedlist contains the circle.
    # Therefore, we use the cycle detection algorithm to find the start of the circle,
    # which is the duplicate exactly!!!
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n <= 1: return -1

        slow = nums[0]
        fast = nums[0]
        flag = 1
        while True:
            if fast == slow and not flag:
                break
            slow = nums[slow]
            fast = nums[nums[fast]]
            flag = 0

        i = nums[0]
        while True:
            if slow == i:
                return i
            else:
                i = nums[i]
                slow = nums[slow]




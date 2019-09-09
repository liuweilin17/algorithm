###########################################
# Let's Have Some Fun
# File Name: 229.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Sep  2 23:31:29 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#229. Majority Element II

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        # use two candidates and two counters
        # an element could be a candidate when it's count is more than x or y
        # where x, y is any two elements in nums
        N = len(nums)
        a1, a2, c1, c2 = 0, 1, 0, 0
        for n in nums:
            if n == a1:
                c1 += 1
            elif n == a2:
                c2 += 1
            elif c1 == 0:
                a1 = n
                c1 += 1
            elif c2 == 0:
                a2 = n
                c2 += 1
            else:
                c1 -= 1
                c2 -= 1

        ret = [e for e in [a1, a2] if nums.count(e) > N//3 ]

        return ret


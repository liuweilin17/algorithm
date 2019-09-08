###########################################
# Let's Have Some Fun
# File Name: 219.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Sep  1 09:42:44 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 219. Contains Duplicate II

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # calculate distance of every pairs of adjacent repeated value in the array
        N = len(nums)
        dt = {}
        for i in range(N):
            if nums[i] in dt:
                if i - dt[nums[i]] <= k:
                    return True
                else:
                    dt[nums[i]] = i
            else:
                dt[nums[i]] = i

        return False

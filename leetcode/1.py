###########################################
# Let's Have Some Fun
# File Name: 1.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Nov 15 12:40:18 2018
###########################################
#coding=utf-8
#!/usr/bin/python

#1. Two Sum

class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dt = {}
        l = len(nums)
        for i in range(l):
            n = nums[i]
            m = target - n
            if m in dt.keys():
                return [dt[m], i]
            else:
                dt[n] = i

if __name__ == '__main__':
    s = Solution()
    ret = s.twoSum([2, 7, 11, 15], 9)
    print(ret)


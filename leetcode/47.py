###########################################
# Let's Have Some Fun
# File Name: 47.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Jan 10 21:29:23 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 47. Permutations II

class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        dt = {} # we use dt instead of list which in Permutations
        for n in nums:
            dt[n] = dt.get(n, 0) + 1
        if len(nums) > 0:
            self.backtrack(dt, len(nums), [], ret)
        return ret

    def backtrack(self, dt, n, tmp, ret):
        if len(tmp) == n and tmp not in ret:
            ret.append(tmp[:])
            return

        for k in dt.keys():
            if dt[k] > 0:
                tmp.append(k)
                dt[k] -= 1
                self.backtrack(dt, n, tmp, ret)
                tmp.pop()
                dt[k] += 1

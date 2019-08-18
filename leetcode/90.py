###########################################
# Let's Have Some Fun
# File Name: 90.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri 16 Aug 23:31:36 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#90. Subsets II

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        nums.sort()
        def helper(tmp, start):
            ret.append(tmp[:])
            i = start
            while i < len(nums):
                # find the length of same elements
                j = i+1
                while j < len(nums):
                    if nums[i] != nums[j]:
                        break
                    j += 1
                for k in range(j-i):
                    tmp.append(nums[i])
                    # begin at j, which not same as nums[i] to remove duplicates
                    helper(tmp[:], j))
                for k in range(j-i):
                    tmp.pop()
                i = j
        helper([], 0)
        return ret






        helper([], 0)
        return ret


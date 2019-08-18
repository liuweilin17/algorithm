###########################################
# Let's Have Some Fun
# File Name: 78.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Jan 10 20:45:04 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 78. Subsets

class Solution:
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ret = []
        self.backtrack(nums, 0, [], ret)
        return ret

    # subsets of begining with nums[start]
    def backtrack(self, nums, start, tmp, ret):
        ret.append(tmp[:])
        for i in range(start, len(nums)):
            tmp.append(nums[i])
            self.backtrack(nums, i+1, tmp, ret)
            tmp.pop()

if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1,2,3,4]))

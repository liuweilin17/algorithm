###########################################
# Let's Have Some Fun
# File Name: 384.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Jan 20 16:06:11 2019
###########################################
#coding=utf-8
#!/usr/bin/python

import random


class Solution:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.origin = nums

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.origin

    def shuffle1(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """

        def backtrack(nums, tmp):
            if len(tmp) == len(nums):
                return tmp
            else:
                candidates = [i for i in nums if i not in tmp]
                tmp.append(candidates[random.randint(0, len(candidates) - 1)])
                return backtrack(nums, tmp)

        return backtrack(self.origin, [])

    def shuffle2(self):
        ret = []
        for i in range(len(self.origin)):
            candidates = [i for i in self.origin if i not in ret]
            ret.append(candidates[random.randint(0, len(candidates) - 1)])
        return ret

    # we do not need to create to list to store the candidates
    def shuffle3(self):
        ret = []
        tmp = self.origin[:]
        for i in range(len(self.origin)):
            ind = random.randrange(len(tmp))
            ret.append(tmp.pop(ind))

        return ret

# Your Solution object will be instantiated and called as such:
obj = Solution([1,2,3])
print(obj.reset())
print(obj.shuffle3())

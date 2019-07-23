###########################################
# Let's Have Some Fun
# File Name: 26.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Nov 16 12:40:02 2018
###########################################
#coding=utf-8
#!/usr/bin/python

#26. Remove Duplicates from Sorted Array

class Solution(object):
    def removeDuplicates1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = -1
        l = len(nums)
        for j in range(l):
            if nums[j] != nums[i] or i == -1:
                i += 1
                nums[i] = nums[j]
        return i+1
    def removeDuplicates2(self, nums: List[int]) -> int:
        if not nums: return 0
        i = 0 # position of last induplicate element
        for j in range(len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i+1


if __name__ == '__main__':
    s = Solution()
    print(s.removeDuplicates([1,1,2]))
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))


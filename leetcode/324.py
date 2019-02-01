###########################################
# Let's Have Some Fun
# File Name: 324.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 29 16:18:11 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#324. Wiggle Sort II

class Solution:
    # brutal method
    def wiggleSort1(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        arr = sorted(nums)
        for i in range(1, len(nums), 2): nums[i] = arr.pop()
        for i in range(0, len(nums), 2): nums[i] = arr.pop()

    # virtual indexing
    def findKth(self, nums, k):
        n = len(nums)
        if n < 1: return None
        pivot = nums[-1]
        i,j = 0,0
        for j in range(n):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
        i -= 1
        if i < k: return self.findKth(nums[i+1:], k-i-1)
        elif i > k: return self.findKth(nums[:i], k)
        else: return nums[i]

    def wiggleSort2(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # find the medium
        n = len(nums)
        medium = self.findKth(nums[:], (n-1)//2)

        # use three way partioning algorithm to partition new array nums[1], nums[3], nums[5], ... and nums[0], nums[2], nums[4], ... based on medium. the bigger ones are in the first array and the smaller ones are in the second array.
        virtual_index = [(2*i + 1) % (n|1) for i in range(n)] # n|1 = n+1 if n is even else n
        i, j, k = 0, 0, n-1
        while j <= k:
            if nums[virtual_index[j]] > medium:
                nums[virtual_index[i]], nums[virtual_index[j]] = nums[virtual_index[j]], nums[virtual_index[i]]
                i += 1
                j += 1
            elif nums[virtual_index[j]] < medium:
                nums[virtual_index[j]], nums[virtual_index[k]] = nums[virtual_index[k]], nums[virtual_index[j]]
                k -= 1
            else:
                j += 1

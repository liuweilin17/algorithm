###########################################
# Let's Have Some Fun
# File Name: 31.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun  2 Jun 17:17:50 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#31. Next Permutation

class Solution:
    # find the first pair i < j where nums[i]<nums[j]
    def nextPermutation1(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        N = len(nums)
        if not N: return

        #partition
        def partition(l, r):
            pivot = nums[r]
            i = l-1
            for j in range(l, r):
                if nums[j] <= pivot:
                    i += 1
                    tmp = nums[j]
                    nums[j] = nums[i]
                    nums[i] = tmp
            nums[r] = nums[i+1]
            nums[i+1] = pivot
            return i+1

        # quick sort
        def quicksort(l, r):
            if l < r:
                p = partition(l, r)
                quicksort(l, p-1)
                quicksort(p+1, r)

        for i in range(N-2, -1, -1):
            minV = None
            for j in range(i+1, N):
                if nums[j] > nums[i]:
                    if minV == None:
                        minV = j
                    elif nums[j] < nums[minV]:
                        minV = j
                    else: pass

            if minV != None:
                tmp = nums[i]
                nums[i] = nums[minV]
                nums[minV] = tmp
                quicksort(i+1, N-1)
                return
        # reverse
        nums.sort()


    # two optimizaton:
    # 1. after finding the pair i<j, nums[i] > nums[j], we could simply reverse nums[i+1:] since there are in reverse order
    # !!!
    # 2. we do not need to use O(n^2) to find the pair!!! Before i is found, nums[i+1:] are in descending order !!!
    def nextPermutation2(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(x,y):
            x, y = i+1, N-1
            while x < y:
                tmp = nums[x]
                nums[x] = nums[y]
                nums[y] = tmp
                x += 1
                y -= 1
        
        N = len(nums)
        if not N: return
        
        # find the first element which is smaller than previous ones
        i = N-2
        while i >= 0:
            if nums[i] >= nums[i+1]:
                i -= 1
            else: break
         
        if i == -1:
            reverse(0, N-1)
            return
        
        j = i+1
        while j < N:
            if nums[j] > nums[i]:
                j += 1
            else:
                break
                
        # swap i, j-1
        tmp = nums[i]
        nums[i] = nums[j-1]
        nums[j-1] = tmp
        
        # reverse i+1,...,N-1
        reverse(i+1, N-1)

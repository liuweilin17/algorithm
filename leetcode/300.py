###########################################
# Let's Have Some Fun
# File Name: 300.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Feb  8 14:54:52 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#300. Longest Increasing Subsequence

class Solution:
    # O(n^2)
    def lengthOfLIS1(self, nums: 'List[int]') -> 'int':
        # d[i], longest length ending at i-th
        # pre[i], i-th pre number
        #pre = {}
        n = len(nums)
        d = [1] * n
        for i in range(1, n):
            p = -1
            for j in range(i):
                if nums[j] < nums[i]:
                    if d[j]+1 > d[i]:
                        d[i] = d[j] + 1
                        #p = j
            #pre[i] = p

        maxL = 0
        #end = 0
        for i in range(n):
            if d[i] > maxL:
                maxL = d[i]
                #end = i

        return maxL

    # notice!!!
    def binarySearch(self, nums, target):
        '''
        @return: insert position
        '''
        n = len(nums)
        if n==0: return -1
        l, m, r = 0, 0, n-1
        while l <= r:
            m = (l+r) // 2
            if nums[m] < target:
                l = m + 1
            elif nums[m] > target:
                r = m - 1
            else:
                return m # found, >=0
        if l == m + 1:
            pos = l
        else:
            pos = r+1
        
        return -pos-1

    # O(nlogn) 
    def lengthOfLIS2(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        d = []
        for i in nums:
            pos = self.binarySearch(d, i)
            if pos < 0:
                pos = -pos-1
                if pos == len(d):
                    d.append(i)
                else:
                    d[pos]=i
            #print(d)
        return len(d)



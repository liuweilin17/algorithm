###########################################
# Let's Have Some Fun
# File Name: 673.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Feb  8 21:34:57 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#673. Number of Longest Increasing Subsequence

class Solution:
    def findNumberOfLIS(self, nums: 'List[int]') -> 'int':
        n = len(nums)
        if n==0: return 0
        d1 = [1] * n #length of longest subsequence ending at i
        d2 = [1] * n #number of longest subseqence ending at i

        for i in range(1, n):
            maxV = 1
            count = 1
            for j in range(i):
                if nums[j] < nums[i]:
                    if d1[j]+1 > maxV:
                        maxV = d1[j]+1
                        count = d2[j]
                    elif d1[j]+1 == maxV:
                        count += d2[j]
            d1[i] = maxV
            d2[i] = count

        #print(d1)
        #print(d2)
        l = max(d1)
        ret = 0
        for i in range(n):
            if d1[i] == l:
                ret += d2[i]

        return ret

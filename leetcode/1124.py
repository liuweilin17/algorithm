###########################################
# Let's Have Some Fun
# File Name: 1124.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun 14 Jul 11:19:07 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#1124. Longest Well-Performing Interval

class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        # create new arr
        N = len(hours)
        a = [0] * (N+1) #a[i] the sum of a[0], ..., a[i-1]
        dt = {}
        maxL = 0
        dt[0] = -1 # the first position of sum0 is 0
        for i in range(1, N+1):
            v = 1 if hours[i-1] > 8 else -1
            a[i] = a[i-1] + v
            if a[i] > 0:
                maxL = max(maxL, i)
            else:
                # dt[a[i]-1] must be smaller than dt[a[i]-2], ...
                # because dt keeps the ealiest position of appearce given value
                if a[i]-1 in dt: # if a[i]-1 does not exist, neither as a[i]-2,...
                    maxL = max(maxL, i-1-dt[a[i]-1]) # the length of interval with sum as 1
            if a[i] not in dt: dt[a[i]] = i-1 # pick the smallest i-1 given value a[i]
        
        # print(a)
        return maxL


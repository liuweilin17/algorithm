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
    def longestWPI1(self, hours: List[int]) -> int:
        N = len(hours)
        hours = [1 if hour > 8 else -1 for hour in hours]
        sumv = 0
        dt = collections.defaultdict(int)
        dt[0] = -1
        max_len = 0
        for i in range(N):
            sumv += hours[i]
            if sumv > 0: # Notice this is important
                max_len = max(max_len, i+1)
            elif sumv-1 in dt: # Simply use sumv since sum is consecutive
                max_len = max(max_len, i-dt[sumv-1])
            else: pass
            if sumv not in dt:
                dt[sumv] = i
        return max_len

    def longestWPI2(self, hours: List[int]) -> int:
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


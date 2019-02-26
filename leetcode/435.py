###########################################
# Let's Have Some Fun
# File Name: 435.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Feb 25 13:40:20 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#435. Non-overlapping Intervals

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def eraseOverlapIntervals(self, intervals: 'List[Interval]') -> 'int':
        # sort
        intervals.sort(key=lambda x:x.start)
        ret = 0
        N = len(intervals)
        if N<= 1: return 0
        t = intervals[0]
        for i in range(1, N):
            lo = max(t.start, intervals[i].start)
            hi = min(t.end, intervals[i].end)
            if lo < hi: # if overlap, keep the interval with the smallest end!!!
                ret += 1
                if hi == intervals[i].end:
                    t = intervals[i]
            else:
                t = intervals[i]

        return ret



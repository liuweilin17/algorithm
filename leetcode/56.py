###########################################
# Let's Have Some Fun
# File Name: 56.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Feb 24 11:24:40 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#56. Merge Intervals

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def merge(self, intervals: 'List[Interval]') -> 'List[Interval]':

        n = len(intervals)
        if n <= 1:
            return intervals

        # sort
        intervals.sort(key=lambda x:x.start)
        ret = []
        t = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i].start <= t.end:
                t = Interval(min(t.start, intervals[i].start), max(t.end, intervals[i].end))
            else:
                ret.append(t)
                t = intervals[i]
        ret.append(t)

        return ret




###########################################
# Let's Have Some Fun
# File Name: 986.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Feb 24 12:21:22 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#986. Interval List Intersections

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        ret = []
        m = len(A)
        n = len(B)
        i, j = 0, 0
        while i < m and j < n:
            lo = max(A[i].start, B[j].start)
            hi = min(A[i].end, B[j].end)
            if hi >= lo: # this is a really treaky to determine the interval!!!
                ret.append(Interval(lo, hi))
            if A[i].end < B[j].end:
                i += 1
            else:
                j += 1

        return ret


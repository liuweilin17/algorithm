###########################################
# Let's Have Some Fun
# File Name: 436.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Feb 25 12:57:45 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#436. Find Right Interval

# Definition for an interval.
# class Interval:
#     def __init__(self, s=0, e=0):
#         self.start = s
#         self.end = e

class Solution:
    def findRightInterval(self, intervals: 'List[Interval]') -> 'List[int]':
        intervals_sort = sorted(intervals, key=lambda x: x.start)
        dt = {}
        N = len(intervals)
        for i in range(N):
            dt[intervals[i]] = i
        ret = []
        for i in range(N):
            int1 = intervals[i]
            #print("{}{}".format(int1.start, int1.end))
            pos = -1
            low, high = 0, N - 1
            while low <= high:
                mid = (low + high) // 2
                if intervals_sort[mid].start > int1.end:
                    high = mid - 1
                elif intervals_sort[mid].start < int1.end:
                    low = mid + 1
                else:
                    pos = dt[intervals_sort[mid]]
                    break
            # low is the position
            if pos == -1:
                if low != N: pos = dt[intervals_sort[low]]
            
            ret.append(pos)

        return ret

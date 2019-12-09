###########################################
# Let's Have Some Fun
# File Name: 252.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Dec  8 18:54:55 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#252. Meeting Rooms

class Solution:
    def canAttendMeetings(self, intervals: List[List[int]]) -> bool:
        if not intervals or not intervals[0]: return True
        s_intervals = sorted(intervals, key=lambda x:x[0])
        N = len(s_intervals)
        for i in range(1, N):
            a, b = s_intervals[i][0], s_intervals[i][1]
            c, d = s_intervals[i-1][0], s_intervals[i-1][1]
            if a < d:
                return False
        return True




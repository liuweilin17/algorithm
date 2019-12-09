###########################################
# Let's Have Some Fun
# File Name: 253.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Nov 17 11:22:20 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#253. Meeting Rooms II

import heapq

class Solution:
    # O(NlogN)
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        N = len(intervals)
        if N <= 0: return 0
        
        
        # sort by start time
        intervals_sort = sorted(intervals, key=lambda x:x[0])
        
        # rooms allocated
        rooms = []
        heapq.heappush(rooms, intervals_sort[0][1])
        for i in range(1, N):
            if rooms[0] <= intervals_sort[i][0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, intervals_sort[i][1])
            
        return len(rooms)
        
        

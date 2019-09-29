###########################################
# Let's Have Some Fun
# File Name: 57.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Sep 25 11:10:15 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#57. Insert Interval

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        def findIns(x): # find the position of x in intervals
            N = len(intervals)
            low, high = 0, N-1
            flag = False # whether x is in an existing interval
            while low <= high:
                mid = low + (high-low) // 2
                if intervals[mid][0] <= x <= intervals[mid][1]:
                    low = mid
                    flag = True
                    break
                elif x < intervals[mid][0]:
                    high = mid - 1
                else:
                    low = mid + 1

            return flag, low

        N = len(intervals)
        flag1, ind1 = findIns(newInterval[0])
        flag2, ind2 = findIns(newInterval[1])
        # print(flag1, ind1, flag2, ind2)
        if flag1:
            if flag2:
                # newInterval[0] and newInterval[1] are in some interval
                return intervals[:ind1] + [[intervals[ind1][0], intervals[ind2][1]]] + intervals[ind2+1:]
            else:
                # newInterval[0] is in some interval, newInterval[1] not
                return intervals[:ind1] + [[intervals[ind1][0], newInterval[1]]] + intervals[ind2:]
        else:
            if flag2:
                # newInterval[1] is in some interval, newInterval[0] not
                return intervals[:ind1] + [[newInterval[0], intervals[ind2][1]]] + intervals[ind2+1:]
            else:
                # newInterval[0] and newInterval[1] are not in some interval
                return intervals[:ind1] + [newInterval] + intervals[ind2:]






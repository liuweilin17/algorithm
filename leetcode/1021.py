###########################################
# Let's Have Some Fun
# File Name: 1021.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Mar 24 18:08:52 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 1021. Best Sightseeing Pair
# Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, 
# and two sightseeing
# spots i and j have distance j - i between them.
# The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : 
# the sum of the values of the sightseeing spots, minus the distance between them.
# Return the maximum score of a pair of sightseeing spots.

class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        cur = 1 # the previous best result
        res = -1 # the final best result
        for a in A:
            res = max(res, cur-1+a)
            cur = max(cur-1, a)
        return res


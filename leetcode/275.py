###########################################
# Let's Have Some Fun
# File Name: 275.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Sep  4 09:16:55 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 275. H-Index II

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        N = len(citations)
        left, right = 1, N
        while left <= right:
            mid = (left + right) // 2
            if citations[N-mid] >= mid:
                left = mid + 1
            else:
                right = mid-1

        return left-1


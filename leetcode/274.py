###########################################
# Let's Have Some Fun
# File Name: 274.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Sep  4 08:43:25 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#274. H-Index

class Solution:
    def hIndex(self, citations: List[int]) -> int:
        citations_sorted = sorted(citations)
        N = len(citations)
        ret = 0
        # h in [1, N]
        for i in range(N, 0, -1):
            if citations_sorted[N-i] >= i:
                ret = i
                break

        return ret

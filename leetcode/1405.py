###########################################
# Let's Have Some Fun
# File Name: 1405.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Apr  5 23:54:11 2020
###########################################
#coding=utf-8
#!/usr/bin/python

#1405. Longest Happy String

from heapq import heappush, heappop

class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        heappush(heap, (-a, 'a'))
        heappush(heap, (-b, 'b'))
        heappush(heap, (-c, 'c'))
        s = ''
        while True:
            c1 = heappop(heap)
            c2 = heappop(heap)
            if c2[0] == 0:
                return s + min(-c1[0], 2)*c1[1]
            c1_n = min(-c1[0], 2)
            s += c1_n * c1[1]

            # this is essential
            c2_n = 1 if c1[0] + c1_n <= c2[0] else 0
            s += c2_n * c2[1]
            heappush(heap, (c1[0]+c1_n, c1[1]))
            heappush(heap, (c2[0]+c2_n, c2[1]))






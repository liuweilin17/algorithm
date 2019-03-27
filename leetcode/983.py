###########################################
# Let's Have Some Fun
# File Name: 983.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Mar 27 11:44:13 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#983. Minimum Cost For Tickets

from functools import lru_cache

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        # dp[i] the min cost of from day i to the end of the day

        @lru_cache(None) # Notice!!! time limit exceed without this
        def dp(i):
            if i > 365:
                return 0
            elif i in days:
                return min(dp(i+1)+costs[0], dp(i+7)+costs[1], dp(i+30)+costs[2])
            else:
                return dp(i+1)

        return dp(1)


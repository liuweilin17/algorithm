###########################################
# Let's Have Some Fun
# File Name: 309.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun 26 May 18:15:42 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#309. Best Time to Buy and Sell Stock with Cooldown

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy[i] maximum profit which end with buying on day i or end with buying on a day before i and takes rest until
        # the day i since then
        # sell[i] maximum profit which end with selling on day i or end with selling on a day before i and takes rest
        # until the day i since then
        # buy[i] = max(buy[i-1], sell[i-2]-prices[i])
        # sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        # b0 = max(b1, s2-prices[i])
        # s0 = max(s1, b1+prices[i])

        N = len(prices)
        if N == 0 or N ==1: return 0

        b0, b1 = 0, -prices[0]
        s0, s1, s2 = 0, 0, 0
        for i in range(1, N):
            b0 = max(b1, s2-prices[i])
            s0 = max(s1, b1+prices[i])
            b1 = b0
            s2 = s1
            s1 = s0

        return s0

###########################################
# Let's Have Some Fun
# File Name: 714.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun 26 May 19:02:13 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#714. Best Time to Buy and Sell Stock with Transaction Fee

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        # buy[i], maximum profit, the last action is buying rather than selling
        # sell[i], maximum profit, the last action is selling rather than buying
        # buy[i] = max(buy[i-1], sell[i-1]-prices[i])
        # sell[i] = max(sell[i-1], buy[i-1]+prices[i]-fee)
        # b0 = max(b1, s1-prices[i])
        # s0 = max(s1, b1+prices[i]-fee)


        N = len(prices)
        if N == 0 or N == 1:
            return 0

        b0, b1 = 0, -prices[0]
        s0, s1 = 0, 0
        for i in range(1, N):
            b0 = max(b1, s1-prices[i])
            s0 = max(s1, b1+prices[i]-fee)
            b1 = b0
            s1 = s0

        return s0



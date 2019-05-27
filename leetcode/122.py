###########################################
# Let's Have Some Fun
# File Name: 122.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat 25 May 12:13:08 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#122. Best Time to Buy and Sell Stock II

class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        if not prices: return 0
        minV = None
        profit = 0
        for price in prices:
            if minV == None or price < minV:
                minV = price
            if price > minV:
                profit += (price - minV)
                minV = price

        return profit

    def maxProfit2(self, prices: List[int]) -> int:
        if not prices: return 0
        N = len(prices)
        profit = 0
        for i in range(1, N):
            if prices[i] > prices[i-1]:
                profit += (prices[i] - prices[i-1])
                
        return profit

    # generate method
     def maxProfit3(self, prices: List[int]) -> int:
        # buy[i], maximum profit, the last action is buying rather than selling
        # sell[i], maximum profit, the last action is selling rather than buying
        # buy[i] = max(buy[i-1], sell[i-1]-prices[i])
        # sell[i] = max(sell[i-1], buy[i-1]+prices[i])
        # b0 = max(b1, s1-prices[i])
        # s0 = max(s1, b1+prices[i])


        N = len(prices)
        if N == 0 or N == 1:
            return 0

        b0, b1 = 0, -prices[0]
        s0, s1 = 0, 0
        for i in range(1, N):
            b0 = max(b1, s1-prices[i])
            s0 = max(s1, b1+prices[i])
            b1 = b0
            s1 = s0

        return s0


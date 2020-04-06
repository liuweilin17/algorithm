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

    # DP, O(N) time, O(N) space
    def maxProfit(self, prices: List[int]) -> int:
        # dp1[i]: the max profit of 0...i, last op is buy
        # dp2[i]: the max profit of 0...i, last op is sell
        N = len(prices)
        if not N: return 0
        dp1 = [0 for _ in range(N)]
        dp1[0] = -prices[0] # last op is buy, so dp1[0] is the price after prices[0] is sold
        dp2 = [0 for _ in range(N)]
        dp2[0] = 0 # last op is sell， at prices[0] no stock is bought, the profit is 0
        for i in range(1, N):
            dp1[i] = max(dp1[i-1], dp2[i-1]-prices[i])
            dp2[i] = max(dp2[i-1], dp1[i-1]+prices[i])
        return max(dp1[N-1], dp2[N-1])

    # DP, O(N) time, O(1) space
    def maxProfit(self, prices: List[int]) -> int:
        N = len(prices)
        if not N: return 0
        a1 = -prices[0]
        a2 = 0
        for i in range(1, N):
            t = a1
            a1 = max(a1, a2-prices[i])
            a2 = max(a2, t+prices[i])
        return a2


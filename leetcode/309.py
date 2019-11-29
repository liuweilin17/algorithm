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
    def maxProfit1(self, prices: List[int]) -> int:
        # buy[i], the maximum profit of 0...i and last op is buy
        # sell[i], the maximum profit of 0...i and last op is sell
        N = len(prices)
        if N <= 1: return 0
        elif N == 2: return max(0, prices[1]-prices[0])
        else:
            buy = [0 for _ in range(N)]
            sell = [0 for _ in range(N)]
            # Notice the initial value of buy and sell
            buy[0] = -prices[0]
            buy[1] = max(-prices[1], -prices[0])
            sell[1] = max(prices[1] - prices[0], 0)
            
            for i in range(2, N):
                buy[i] = max(buy[i-1], sell[i-2]-prices[i])
                sell[i] = max(sell[i-1], buy[i-1]+prices[i])
            return max(buy[N-1], sell[N-1])

    def maxProfit2(self, prices: List[int]) -> int:
        # buy[i], the maximum profit of 0...i and last op is buy
        # sell[i], the maximum profit of 0...i and last op is sell
        N = len(prices)
        if N <= 1: return 0
        elif N == 2: return max(0, prices[1]-prices[0])
        else:
            # Notice the initial value of buy and sell
            b0 = -prices[0]
            b1 = max(-prices[1], -prices[0])
            s0 = 0
            s1 = max(prices[1] - prices[0], 0)

            for i in range(2, N):
                b2 = max(b1, s0-prices[i])
                s2 = max(s1, b1+prices[i])
                b1 = b2
                s0 = s1
                s1 = s2
            return s2

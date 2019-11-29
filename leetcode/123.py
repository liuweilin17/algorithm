###########################################
# Let's Have Some Fun
# File Name: 123.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Oct 19 17:09:01 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 123. Best Time to Buy and Sell Stock III

class Solution:
    def maxProfit1(self, prices: List[int]) -> int:
        # two transactions
        firstBuy, firstSell = float('inf'), 0
        secondBuy, secondSell = float('inf'), 0
        for p in prices:
            firstBuy = min(firstBuy, p)
            firstSell = max(firstSell, p-firstBuy)
            secondBuy = min(secondBuy, p-firstSell)
            secondSell = max(secondSell, p-secondBuy)
        return secondSell

    def maxProfit2(self, prices: List[int]) -> int:
        K = 2 # number of transactions
        N = len(prices)
        if N == 0 or N == 1: return 0

        g = [0 for _ in range(K+1)]
        f = [0 for _ in range(K+1)]

        for i in range(1, N):
            tmp = f[0]
            for j in range(1, K+1):
                g[j] = max(g[j], tmp) + prices[i] - prices[i-1]
                tmp = f[j] # all use old f
                f[j] = max(f[j], g[j])

        return f[K]


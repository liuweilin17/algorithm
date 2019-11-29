###########################################
# Let's Have Some Fun
# File Name: 188.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Oct 19 17:17:15 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 188. Best Time to Buy and Sell Stock IV

class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        # t[i][j] maximum profit with i transactions and in 0...j days
        N = len(prices)
        if N == 0 or N == 1: return 0
        if k > N//2:
            profits = 0
            for i in range(1, N):
                if prices[i] > prices[i-1]:
                    profits += prices[i] - prices[i-1]
            return profits
        
        t = [[0 for _ in range(N)] for _ in range(k+1)]
        for i in range(1, k+1):
            tmpMaxP = -prices[0]
            for j in range(1, N):
                # t[i][j-1]: do not sell or buy on prices[j]
                # prices[j] + tmpMaxP: sell at prices[j] + previous max profits tmpMaxP
                t[i][j] = max(t[i][j-1], prices[j]+tmpMaxP)
                tmpMaxP = max(tmpMaxP, t[i-1][j-1]-prices[j])
        return t[k][N-1]

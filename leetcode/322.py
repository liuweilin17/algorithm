###########################################
# Let's Have Some Fun
# File Name: 322.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Jan 13 21:53:12 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 322. Coin Change
# This is a variation of Knapsack problem
# dynamic programming
# we should see the solution in the second round

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        inf = amount + 1
        l = len(coins)
        coins.sort()
        d = [] #d[i][w], the first i+1 coins making w money
        # initialize
        for i in range(l):
            d.append([0] * (amount+1))
        # calculate d[0][w]
        for i in range(amount+1):
            d[0][i] = i / coins[0] if not i % coins[0] else inf
        # calculate the rest
        for i in range(1, l):
            for j in range(amount+1):
                if j < coins[i]:
                    d[i][j] = d[i-1][j]
                else:
                    # d[i-1][j]: not use coins[i], d[i][j-coins[i]]: use coins[i]
                    d[i][j] = min(d[i-1][j], d[i][j-coins[i]]+1)
        if d[l-1][amount] == inf:
            return -1
        else:
            return d[l-1][amount]

if __name__ == '__main__':
    s = Solution()




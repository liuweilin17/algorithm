###########################################
# Let's Have Some Fun
# File Name: 518.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Jan 14 17:43:56 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# Ecopia2
# 518. Coin Change 2
# Knapsack problem, similar to 322

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        if len(coins) < 1:
            if amount == 0:
                return 1
            else:
                return 0

        # d[i][w]: using the first (i+1) denominations making w money

        # initialize
        d = []
        l = len(coins)
        for i in range(l):
            d.append([0] * (amount + 1))

        # sort the coin
        coins.sort()

        # when i = 0
        for i in range(amount + 1):
            if not i % coins[0]:
                d[0][i] = 1
            # else:
            #    d[0][i] = 0

        # calculate d[i][w]
        for i in range(1, l):
            for j in range(amount + 1):
                if j < coins[i]:
                    d[i][j] = d[i - 1][j]
                else:
                    # d[i-1][j]: not using coins[i], d[i][j-coins[i]]: using coins[i]
                    d[i][j] = d[i - 1][j] + d[i][j - coins[i]]

        return d[l - 1][amount]

if __name__ == '__main__':
    s = Solution()
    print(s.change(5, [1,2,5]))
    print(s.change(0, []))
    print(s.change(1, []))

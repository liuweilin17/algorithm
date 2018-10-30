###########################################
# Let's Have Some Fun
# File Name: 121.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Oct 30 12:23:23 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 121. Best Time to Buy and Sell Stock
# 解题思路：
# 遍历数组，记录当前最大值和最小值以及位置
# 如果出现 比当前最小值还小的值，则计算当前利润，更新最大利润，更新最小值，初始化最大值；
# 因为如果之后出现更高的值的时候，肯定会使用当前的最小值作为买入价。
# 如果出现 比当前最大值还大的值，则更新最大值，当前买入肯定比之前利润更高。
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        maxV = -100000
        minV = 100000
        minP = -1
        maxP = -1
        maxPro = 0
        for i in range(l):
            if prices[i] < minV:
                if maxP != -1:
                    maxPro = maxPro if maxV-minV < maxPro else maxV-minV
                    maxV = -100000
                    minV = prices[i]
                    minP = i
                    maxP = -1
                else:
                    minV = prices[i]
                    minP = i
            if prices[i] > maxV:
                if i > minP and minP != -1 and prices[i] > minV:
                    maxV = prices[i]
                    maxP = i 
        return maxPro if maxPro > maxV-minV else maxV-minV

if __name__ == '__main__':
    s = Solution()
    prices = [7,1,5,3,6,4]
    print s.maxProfit(prices)
    prices = [7,6,4,3,1]
    print s.maxProfit(prices)
    prices = [2,4,1]
    print s.maxProfit(prices)

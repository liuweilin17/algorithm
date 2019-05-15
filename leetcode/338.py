###########################################
# Let's Have Some Fun
# File Name: 338.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue 14 May 10:06:17 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#338. Counting Bits

class Solution:
    def countBits(self, num: int) -> List[int]:
        dp = [0]
        for i in range(1, num+1):
            t = i >> 1
            if i % 2 == 0:
                dp.append(dp[t])
            else:
                dp.append(dp[t] + 1)

        return dp



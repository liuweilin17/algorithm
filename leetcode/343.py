###########################################
# Let's Have Some Fun
# File Name: 343.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Sep  7 21:19:07 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 343. Integer Break

class Solution:
    def integerBreak1(self, n: int) -> int:
        # dp[n] the maximum product with sum of n
        dp = [1] * (n+1)
        for i in range(2, n+1):
            t = 0
            for j in range(1, i):
                t = max([t, dp[i-j]*dp[j], dp[i-j]*j, (i-j)*j])
            dp[i] = t
        # print(dp)
        return dp[n]

    # math solution
    def integerBreak2(self, n: int) -> int:
        # if N is only divided into two number, then
        # N//2, N//2 if N is even
        # (N-1)//2, (N+1)//2 if N is odd
        # after N is divided into two parts, for each part
        # it should be broken when
        # M <= (M//2) * (M//2) (M is even) => M >= 4
        # M <= (M-1)//2 * (M+1)//2 (M is odd) => M >= 5
        # that is to say
        # N should be divided into 2 or 3
        # since 2*2*2 <= 3*3, 2 should not appear more than two times
        if n == 2: return 1
        if n == 3: return 2
        ret = 1
        while n > 4:
            ret *= 3
            n -= 3
        ret *= n
        return ret



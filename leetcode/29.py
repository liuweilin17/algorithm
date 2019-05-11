###########################################
# Let's Have Some Fun
# File Name: 29.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat 11 May 11:41:22 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#29. Divide Two Integers

class Solution:
    # calculates number of substraction of dividend by divisor before dividend < divisor
    def divide(self, dividend: int, divisor: int) -> int:
        pos = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        ret = 0
        while dividend >= divisor:
            tmp, i = divisor, 1
            # multiplies tmp by 2 each time to accelerate the updates of devidend faster
            while dividend >= tmp:
                dividend -= tmp
                ret += i
                tmp <<= 1
                i <<= 1

        if pos:
            return min(ret, 2 ** 31 - 1) # 32-signed int: [-2^31, 2^31-1]
        else:
            return -ret


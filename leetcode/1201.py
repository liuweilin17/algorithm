###########################################
# Let's Have Some Fun
# File Name: 1201.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Sep 22 17:46:18 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#1201. Ugly Number III

import math

class Solution:
    def nthUglyNumber(self, n: int, a: int, b: int, c: int) -> int:
        # calculate the least common multiple
        ab = a*b//math.gcd(a,b)
        ac = a*c//math.gcd(a,c)
        bc = b*c//math.gcd(b,c)
        abc = a*bc // math.gcd(a, bc)
        # print(ab, ac, bc, abc)

        # binary search
        low, high = 1, 2*pow(10, 9)
        while low <= high:
            mid = low + (high-low)//2
            candi = mid//a + mid//b + mid//c - mid//ab - mid//ac - mid//bc + mid//abc
            if candi < n:
                low = mid + 1
            elif candi >= n:
                high = mid - 1

        return low




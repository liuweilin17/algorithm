###########################################
# Let's Have Some Fun
# File Name: 201.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu 29 Aug 11:26:01 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#201. Bitwise AND of Numbers Range

class Solution:
    def rangeBitwiseAnd(self, m: int, n: int) -> int:
        # 1. if m != n, last bit is 0
        # 2. >> m and n
        # 3. repeat 1 until m == n.
        # In the same time, we need to keep << times and multiply m with 2^(>> times)

        move = 1
        while m != n:
            if m == 0: return 0
            m >>= 1
            n >>= 1
            move *= 2
        return move * m

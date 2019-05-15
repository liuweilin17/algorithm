###########################################
# Let's Have Some Fun
# File Name: 461.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat 11 May 16:22:30 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#461. Hamming Distance

class Solution:
    # XOR and calculate the number of 1s
    def hammingDistance(self, x: int, y: int) -> int:
        z = x ^ y
        res = 0
        while z > 0:
            res += z & 1
            z >>= 1

        return res


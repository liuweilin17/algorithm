###########################################
# Let's Have Some Fun
# File Name: 231.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Sep  2 10:32:03 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#231. Power of Two

class Solution:
    # & for several times
    def isPowerOfTwo1(self, n: int) -> bool:
        while n:
            if n&1 == 1:
                break
            else:
                n >>= 1

        return True if n == 1 else False
   
   # & for just one time
    def isPowerOfTwo2(self, n: int) -> bool:
        if n <= 0: return False
        return True if not n&(n-1) else False





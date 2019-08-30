###########################################
# Let's Have Some Fun
# File Name: 168.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed 28 Aug 00:22:14 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#168. Excel Sheet Column Title

class Solution:
    # minus one each time to make it from 1 ... 26 to 0 ... 25,
    # which 26 jin zhi
    def convertToTitle(self, n: int) -> str:
        ret = ""
        while n>0:
            n -= 1
            ret = chr(ord('A') + n % 26) + ret
            n //= 26
        return ret


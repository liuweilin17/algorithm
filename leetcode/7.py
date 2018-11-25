###########################################
# Let's Have Some Fun
# File Name: 7.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Nov 25 00:57:41 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 7. Reverse Integer

class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        ret = 0
        flag = False
        if x < 0:
            x = -x
            flag = True
        while x:
            ret = ret * 10 + x % 10
            x = int(x / 10)
        if ret > 2 ** 31 - 1:
            ret = 0
        if flag:
            ret = -ret
        return ret


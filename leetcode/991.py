###########################################
# Let's Have Some Fun
# File Name: 991.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Feb 10 16:05:41 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#991. Broken Calculator

class Solution:
    # it actually uses greedy !
    # math is crazy !!!
    # it's impossible to use dp, since the substructure is unstable
    def brokenCalc(self, X: 'int', Y: 'int') -> 'int':
        ans = 0
        while Y > X:
            ans += 1
            if Y % 2: Y += 1
            else: Y //= 2
        return ans + (X-Y)

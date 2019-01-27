###########################################
# Let's Have Some Fun
# File Name: 984.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Jan 26 23:56:12 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 984. String Without AAA or BBB
# I think this so called easy question is not easy!!!
# let's suppose A > B, to make it easier to explain.
# if no aaa, bbb, then the sequence is mixed with 'aabaabaab...' or 'ababab...'
# therefore, we need to decompose A, B as, A = a1 + a2, B = b1 + b2, a1 = 2b1, a2=b2
class Solution:
    def strWithout3a3b(self, A, B):
        """
        :type A: int
        :type B: int
        :rtype: str
        """
        if A == 0 or B == 0: return A * 'a' + B * 'b'

        ret = ''
        a = A
        b = B
        if A > B:
            while b>0 and a // b <= 1:
                b -= 1
                a -= 1
            ret += b * 'aab'
            a = A - 2 * b
            b = B - b
            if a > b:
                ret += b * 'ab' + (a - b) * 'a'
            else:
                ret += a * 'ba' + (b - a) * 'b'
        else:
            while a>0 and b // a <= 1:
                a -= 1
                b -= 1
            ret += a * 'bba'
            b = B - 2 * a
            a = A - a
            if a > b:
                ret += b * 'ab' + (a - b) * 'a'
            else:
                ret += a * 'ba' + (b - a) * 'b'
        return ret

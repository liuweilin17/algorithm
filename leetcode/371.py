###########################################
# Let's Have Some Fun
# File Name: 371.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Oct  4 13:25:09 2018
# Sum of Two Integers
###########################################
#coding=utf-8
#!/usr/bin/python
import math

class Solution(object):
    # Reason is Python use infinite number of bits so the loop never terminates.
    # Reference here: https://wiki.python.org/moin/BitwiseOperators
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xffffffff
        maxV = 0xefffffff
        if a == 0:
            return b
        if b == 0:
            return a
        while(b != 0):
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry
        return a if a<=maxV else ~(a ^ mask)

if __name__ == '__main__':
    s = Solution()
    print s.getSum(3,3)
    print s.getSum(2,-3)
    print s.getSum(1,-1)
    print s.getSum(-1,1)
    print s.getSum(16,-14)

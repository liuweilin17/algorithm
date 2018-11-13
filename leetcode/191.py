###########################################
# Let's Have Some Fun
# File Name: 191.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Nov 13 18:05:09 2018
###########################################
#coding=utf-8
#!/usr/bin/python

class Solution(object):

	# brutal way
    def hammingWeight1(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n > 0:
            #print(n)
            b = int(n % 2)
            if b == 1:
                ret += 1
            n = int(n / 2)
        return ret

	def hammingWeight3(self, n):
        """
        :type n: int
        :rtype: int
        """
        mask = 1
        ret = 0
        for i in range(32):
            if n & mask != 0:
               ret += 1
            mask <<= 1
        return ret

	# n & n-1 turn the least significant 1 to 0
	def hammingWeight3(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n>0:
            n &= n-1
            ret += 1
        return ret

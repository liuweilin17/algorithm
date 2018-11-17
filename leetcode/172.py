###########################################
# Let's Have Some Fun
# File Name: 172.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Nov 16 20:41:24 2018
###########################################
#coding=utf-8
#!/usr/bin/python

#172. Factorial Trailing Zeroes

class Solution(object):
    # 2^x * 5^x has x trailing zeros
    # for example
    # 5, 10, 15, 20,... * odd has 0
    # 25, 50, 75 * 4i has 00
    # therefore, we try to count the number of 5*1, 25*2, 125*3,...

    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        ret = 0
        while n>0:
            ret += int(n / 5)
            n = int(n / 5)
        return ret


if __name__ == '__main__':
    s = Solution()
    print(s.trailingZeroes(3))
    print(s.trailingZeroes(5))


###########################################
# Let's Have Some Fun
# File Name: 69.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Nov 23 01:55:36 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 69. Sqrt(x))

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x < 0:
            return None

        a = int((x + 2) / 2)
        while True:
            b = int(x/a)
            if a - b >= -1 and a - b <= 1:
                return min(a,b)
            else:
                a = int((a+b)/2)

if __name__ == '__main__':
    s = Solution()
    s.mySqrt()


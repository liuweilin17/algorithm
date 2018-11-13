###########################################
# Let's Have Some Fun
# File Name: 326.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Nov 13 16:21:11 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 326. Power of Three

class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        while n > 0:
            mod = int(n % 3)
            if mod != 0 and n != 1:
                return False
            else:
                n /= 3
        return True

    # convert n to base 3
    # and it should be like 1000...00
    def isPowerOfThree1(self, n):
        pass

if __name__ == '__main__':
    s = Solution()
    testCase = [27, 0, 9, 45, -3]
    for n in testCase:
        print(s.isPowerOfThree(n))


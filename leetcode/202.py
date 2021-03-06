###########################################
# Let's Have Some Fun
# File Name: 202.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Nov  9 11:31:41 2018
###########################################
#coding=utf-8
#!/usr/bin/python
import math

# 202. Happy Number
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        rec = []
        while True:
            n_new = 0
            while n:
               n_new += math.pow(n%10, 2)
               n /= 10
            n_new = int(n_new)
            if n_new == 1:
                return True
            elif n_new in rec:
                return False
            else:
                rec.append(n_new)
                n = n_new

    def isHappy1(self, n: int) -> bool:
        def getSum(n):
            sum_ = 0
            while n:
                a = n%10
                sum_ += a * a
                n //= 10
            return sum_

        # the process would repeat in a loop
        slow, fast = n, n
        while True:
            slow = getSum(slow)
            fast = getSum(getSum(fast))
            if slow == 1:
                return True
            elif slow == fast:
                return False
            else: pass

if __name__ == '__main__':
    s = Solution()
    print s.isHappy(19)
    print s.isHappy(20)
    print s.isHappy(18)
    print s.isHappy(10)

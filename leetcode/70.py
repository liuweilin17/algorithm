###########################################
# Let's Have Some Fun
# File Name: 70.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Nov  9 12:06:13 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 70. Climbing Stairs
# case 1: the last step is one step: a[n-1]
# case 2: the last step is two step: a[n-2]
class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n<1:
            return 0
        a = []
        a.append(1)
        a.append(1)
        for i in range(2,n+1):
            a.append(a[i-1] + a[i-2])
        return a[n]

if __name__ == '__main__':
    s = Solution()
    print s.climbStairs(2)
    print s.climbStairs(3)

###########################################
# Let's Have Some Fun
# File Name: 62.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Jan 25 22:07:08 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#62. Unique Paths

class Solution:
    # math
    def uniquePaths1(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        a = m + n - 2
        b = m - 1
        ret = 1
        for i in range(b):
            ret *= a
            a -= 1
        c = 1
        for i in range(1, b+1):
            c *= i
        #print(ret)
        #print(c)
        return ret//c
    
    # dynamic programming
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        d = []
        # all the entries are initialized as 1, which saves the time.
        for i in range(m):
            d.append([1]*n)
            
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i-1][j] + d[i][j-1]
        
        return d[m-1][n-1]
                  

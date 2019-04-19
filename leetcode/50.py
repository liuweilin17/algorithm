###########################################
# Let's Have Some Fun
# File Name: 50.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Mar 29 15:12:32 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#50. Pow(x, n)

class Solution:
    def myPow1(self, x: float, n: int) -> float:
        return x**n

    def myPow2(self, x: float, n: int) -> float:
        # n == 0
        if n == 0:
            return 1
        elif n < 0:
            x = 1 / x
            n = -n
            return x ** n
        else:
            return (x*x)**(n // 2) if n%2 == 0 else x * ((x*x)**(n // 2))


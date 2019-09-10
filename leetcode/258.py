###########################################
# Let's Have Some Fun
# File Name: 258.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Sep  3 09:15:20 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#258. Add Digits

class Solution:
    def addDigits1(self, num: int) -> int:
        def helper(n):
            ret = 0
            while n:
                ret += n % 10
                n //= 10
            return ret

        while num >= 10:
            num = helper(num)

        return num

    def addDigits2(self, num: int) -> int:
        if num == 0:
            return 0
        else:
            return (num - 1) % 9 + 1





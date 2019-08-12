###########################################
# Let's Have Some Fun
# File Name: 415.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed 10 Jul 13:46:02 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#415. Add Strings

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        N1, N2 = len(num1), len(num2)
        ret = [0] * (max(N1, N2) + 1)
        for i in range(1, max(N1, N2)+1):
            x = int(num1[-i]) if i <= N1 else 0
            y = int(num2[-i]) if i <= N2 else 0
            sumV = ret[-i] + x + y
            ret[-i] = sumV % 10
            ret[-i-1] += sumV // 10
        # print(ret)
        s = ''.join(map(str, ret)).lstrip('0')
        return s if s else "0"


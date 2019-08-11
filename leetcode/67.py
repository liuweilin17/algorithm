###########################################
# Let's Have Some Fun
# File Name: 67.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed 10 Jul 13:52:00 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#67. Add Binary

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        N1, N2 = len(a), len(b)
        ret = [0] * (max(N1, N2) + 1)
        for i in range(1, max(N1, N2)+1):
            x = int(a[-i]) if i <= N1 else 0
            y = int(b[-i]) if i <= N2 else 0
            sumV = ret[-i] + x + y
            ret[-i] = sumV % 2
            ret[-i-1] += sumV // 2

        s = ''.join(map(str, ret)).lstrip('0')
        return s if s else "0"


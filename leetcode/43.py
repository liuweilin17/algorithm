###########################################
# Let's Have Some Fun
# File Name: 43.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed 10 Jul 10:38:56 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#43. Multiply Strings

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        N1, N2 = len(num1), len(num2)
        ret = [0] * (N1 + N2)
        for i in range(N1-1, -1, -1):
            for j in range(N2-1, -1, -1):
                sumV = ret[i+j+1] + (int(num1[i]) * int(num2[j]))
                ret[i+j+1] = sumV % 10 # Notice it's '=' instead of '+='
                ret[i+j] += sumV // 10 # Notice it's '+=' instead of '='

        # print(ret)
        s = ''.join(map(str, ret))
        s = s.lstrip('0')
        return s if s else '0'



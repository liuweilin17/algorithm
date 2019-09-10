###########################################
# Let's Have Some Fun
# File Name: 306.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Sep  4 22:27:43 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 306. Additive Number

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        # if str n could be additive sequence
        # with [0:first], [first:second]
        def helper(first, second, s):
            if second == len(s):
                return True
            fir, sec = s[:first], s[first:second]
            if len(fir) > 1 and fir.find("0") == 0 or \
            len(sec) > 1 and sec.find("0") == 0:
                return False
            fir, sec = int(fir), int(sec)
            thir = str(fir + sec)

            if s[second:].find(thir) == 0:
                # print(fir, sec, thir)
                return helper(second-first,second+len(thir)-first, s[first:])

        N = len(num)
        # return helper(1, 3, num)
        for i in range(1, N-1):
            for j in range(i+1, N):
                if helper(i, j, num):
                    return True

        return False


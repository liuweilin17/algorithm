###########################################
# Let's Have Some Fun
# File Name: 6.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat  6 Jul 11:21:19 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#6. ZigZag Conversion

class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if not s: return ''
        x = 0
        step = 1
        dt = collections.defaultdict(list)
        for c in s:
            dt[x].append(c)
            if x == numRows - 1:
                step = -1
            elif x == 0:
                step = 1
            else: pass
            x += step

        ret = ''
        for key in dt:
            ret += ''.join(dt[key])
        return ret


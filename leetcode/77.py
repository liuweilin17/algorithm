###########################################
# Let's Have Some Fun
# File Name: 77.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Feb  9 14:58:08 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#77. Combinations

class Solution:
    def combine(self, n: 'int', k: 'int') -> 'List[List[int]]':
        def backtrack(n, k, tmp, ret, t):
            if len(tmp) == k:
                ret.append(tmp[:])
            else:
                for i in range(t, n+1):
                    bak = tmp[:]
                    bak.append(i)
                    backtrack(n, k, bak, ret, i+1)

        if n < k or n < 1: return [[]]

        ret = []
        backtrack(n, k, [], ret, 1)
        return ret


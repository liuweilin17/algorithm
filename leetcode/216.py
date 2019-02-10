###########################################
# Let's Have Some Fun
# File Name: 216.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Feb  9 15:33:31 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#216. Combination Sum III

class Solution:
    def combinationSum3(self, k: 'int', n: 'int') -> 'List[List[int]]':
        def backtrack(k, n, tmp, ret, t):
            if n == 0 and k==0:
                ret.append(tmp[:])
            elif n > 0 and k > 0:
                for i in range(t, 10):
                    if i <= n:
                        bak = tmp[:]
                        bak.append(i)
                        backtrack(k-1, n-i, bak, ret, i+1)
            else:
                pass

        if k<1 or n<1: return [[]]

        ret = []
        backtrack(k, n, [], ret, 1)

        return ret


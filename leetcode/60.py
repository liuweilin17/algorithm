###########################################
# Let's Have Some Fun
# File Name: 60.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat 13 Jul 16:53:17 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#60. Permutation Sequence

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        def countP(n):
            ret = 1
            for i in range(1, n+1): ret *= i
            return ret

        ret = []
        for i in range(n):
            ind, mod = k // countP(n-1-len(ret)), k % countP(n-1-len(ret))
            ind = ind if mod > 0 else max(ind-1, 0)
            mod = mod if mod > 0 else countP(n-1-len(ret))
            for j in range(1, n+1): # ind of unseen elements in 1...n
                if j not in ret:
                    if ind == 0:
                        ret.append(j)
                        break
                    ind -= 1
            k = mod

        return ''.join(map(str, ret))

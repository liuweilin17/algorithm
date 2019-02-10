###########################################
# Let's Have Some Fun
# File Name: 39.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Feb  9 15:09:10 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#39. Combination Sum

class Solution:
    def combinationSum(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        def backtrack(candidates, target, tmp, ret, t):
            if target == 0:
                ret.append(tmp[:])
            elif target > 0:
                for i in range(t, len(candidates)):
                    if candidates[i] <= target: #notice '<=' not '<' !!!
                        bak = tmp[:]
                        bak.append(candidates[i])
                        backtrack(candidates, target-candidates[i], bak, ret, i)
            else:
                pass

        if not candidates: return [[]]
        ret = []
        backtrack(candidates, target, [], ret, 0)

        return ret




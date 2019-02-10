###########################################
# Let's Have Some Fun
# File Name: 40.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Feb  9 15:24:37 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#40. Combination Sum II

class Solution:
    def combinationSum2(self, candidates: 'List[int]', target: 'int') -> 'List[List[int]]':
        def backtrack(condidates, target, tmp, ret, t):
            if target == 0:
                if tmp not in ret:
                    ret.append(tmp[:])
            elif target > 0:
                for i in range(t, len(candidates)):
                    if candidates[i] <= target:
                        bak = tmp[:]
                        bak.append(candidates[i])
                        backtrack(candidates, target-candidates[i], bak, ret, i+1)
            else:
                pass

        if not candidates: return [[]]

        ret = []
        candidates = sorted(candidates)
        backtrack(candidates, target, [], ret, 0)

        return ret


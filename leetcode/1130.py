###########################################
# Let's Have Some Fun
# File Name: 1130.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun 21 Jul 14:23:36 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#1130. Minimum Cost Tree From Leaf Values

class Solution:
    # cache + recursion
    # tree question could mostly be solved by recursion
    def mctFromLeafValues(self, arr: List[int]) -> int:
        dt = {}
        def helper(begin, end):
            if (begin, end) in dt: return dt[(begin, end)]
            N = len(arr)
            if end - begin <= 1: return 0
            else:
                ret = 2 ** 31
                for i in range(begin+1, end):
                    ret = min(ret, helper(begin, i)+helper(i, end)+max(arr[begin:i])*max(arr[i:end]))
                dt[(begin, end)] = ret
                return ret

        return helper(0, len(arr))



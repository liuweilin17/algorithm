###########################################
# Let's Have Some Fun
# File Name: 399.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri May 17 17:06:05 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#399. Evaluate Division

import collections

class Solution:
    # simply use dfs in graph
    def calcEquation(self, equations, values, queries):
        N1, N2 = len(equations), len(queries)
        if not N1: return [-1.0] * N2

        adj_list = collections.defaultdict(list)
        for i in range(N1):
            op1, op2 = equations[i]
            val = values[i]
            adj_list[op1].append((op2, val))
            if val != 0:
                adj_list[op2].append((op1, 1.0 / val))

        seen = []
        def dfs(n1, n2):
            seen.append(n1)
            if n1 not in adj_list:
                return -1.0
            elif n2 not in adj_list:
                return -1.0
            elif n1 == n2:
                return 1.0
            else:
                for nd, v in adj_list[n1]:
                    if nd not in seen:
                        t = dfs(nd, n2)
                        if t != -1:
                            # Notice you cannot use v * dfs(nd, v2) !!!
                            # if you call dfs again, it will return -1 since nd is added to seen
                            return v * t 
                return -1

        ret = []
        for i in range(N2):
            seen = []
            res = dfs(queries[i][0], queries[i][1])
            ret.append(res)

        return ret


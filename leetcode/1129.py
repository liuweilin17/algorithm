###########################################
# Let's Have Some Fun
# File Name: 1129.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun 21 Jul 13:15:21 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 1129. Shortest Path with Alternating Colors

class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        g = collections.defaultdict(list)
        for e in red_edges:
            g[e[0]].append((e[1], 0))
        for e in blue_edges:
            g[e[0]].append((e[1], 1))

        # BFS, node with different color edges are considered as different nodes
        visited = [[0, 0], [0, 1]] # i, c: node, color
        # res = [[0, 0]] + [[2*n, 2*n]] * (n-1) # Notice that that last n-1 elements are shallow copy !!!!!!
        res = [[0, 0]] + [[2*n, 2*n] for i in range(n-1)] # dist starting with red, dist starting with blue
        for i, c in visited: # iterate a incremented array as a queue
            print(len(g[i]))
            for j, cc in g[i]:
                if cc == c: continue
                elif res[j][cc] == 2*n:
                    res[j][cc] = res[i][c] + 1
                    visited.append([j, cc])
            print(res)
        ret = []
        for d1, d2 in res:
            ret.append(min(d1, d2) if min(d1, d2) < 2*n else -1)
        return ret








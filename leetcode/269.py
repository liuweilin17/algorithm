###########################################
# Let's Have Some Fun
# File Name: 269.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Dec  8 22:39:30 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#269. Alien Dictionary

import collections

class Solution:
    def alienOrder(self, words: List[str]) -> str:
        N = len(words)
        if not N: return ""

        graph = collections.defaultdict(list)
        alphas = [c for c in words[0]]
        # build graph
        for i in range(1, N):
            pre = words[i-1]
            cur = words[i]
            alphas += [c for c in cur]
            N1, N2 = len(pre), len(cur)
            i = 0
            while i < N1 and i < N2:
                if pre[i] != cur[i]:
                    graph[pre[i]].append(cur[i])
                    break
                i += 1
        alphas = list(set(alphas))

        def dfs(c):
            color[c] = 1
            self.cur += 1
            for nei in graph[c]:
                if color[nei] == 0:
                    dfs(nei)
                elif color[nei] == 1:
                    self.flag = False
                    return
            color[c] = 2
            self.ret.append(c)

        # topological sort
        self.ret = []
        self.flag = True
        color = collections.defaultdict(int) # 0: unvisited, 1: grey, 2: black
        self.cur = 0
        for c in alphas:
            if color[c] == 0:
                dfs(c)
        return "".join(self.ret[::-1]) if self.flag else ""



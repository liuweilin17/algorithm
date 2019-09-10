###########################################
# Let's Have Some Fun
# File Name: 310.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Sep  5 22:27:45 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 310. Minimum Height Trees

class Solution:
    # time limit exceed
    def findMinHeightTrees1(self, n: int, edges: List[List[int]]) -> List[int]:
        # adjacent list
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        def dfs(num, visited):
            ret = 0
            for neighbor in g[num]:
                if neighbor not in visited:
                    ret = max(ret, dfs(neighbor, visited + [num])+1)
            return ret


        ret = []
        min_height = n
        for i in range(n):
            # try i as root and cal_length
            height = dfs(i, [])
            # print(i, height)
            if height == min_height:
                ret.append(i)
            elif height < min_height:
                ret = [i]
                min_height = height
            else: pass

        return ret

    
    # nong cun bao wei cheng shi
    def findMinHeightTrees2(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1: return [0]

        # adjacent list
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)

        # keep finding the leaves
        # the remaining 1 or 2 leaves are the root !!!
        # similar to method 2 of topological sort

        leaves = []
        for i in range(n):
            if len(g[i]) == 1:
                leaves.append(i)

        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = g[i].pop()
                g[j].remove(i)
                if len(g[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves

        return leaves

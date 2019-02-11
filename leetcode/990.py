###########################################
# Let's Have Some Fun
# File Name: 990.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Feb 10 15:54:06 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#990. Satisfiability of Equality Equations
# This question has two methods, which are connected components and union find
# They are both very useful but not fimiliar to me !!!!!

import string

class Solution(object):
    # Union find(https://www.cs.princeton.edu/~rs/AlgsDS07/01UnionFind.pdf)
    def equationsPossible1(self, equations):
        # Union find, # uf[x] is the category of x
        def root(x):
            while x != id[x]: x = id[x]
            return x

        def unite(a, b):
            root1 = root(a)
            root2 = root(b)
            id[root1] = root2

        id = {a:a for a in string.ascii_lowercase}

        for a, e, _, b in equations:
            if e == '=':
                unite(a, b)
        for a, e, _, b in equations:
            if e == '!':
                if root(a) == root(b):
                    return False
        return True

    # Union find improvements
    def equationsPossible2(self, equations):
        def root(x):
            while x != id[x]:
                # improvements: make every other node in path point to its grandparent
                # so as to make the tree flat
                id[x] = id[id[x]]
                x = id[x]
            return x

        def unite(a, b):
            root1 = root(a)
            root2 = root(b)
            id[root1] = root2

        id = {a:a for a in string.ascii_lowercase}
        for a, e, _, b in equations:
            if e == '=':
                unite(a, b)

        for a, e, _, b in equations:
            if e == '!':
                if root(a) == root(b):
                    return False
        return True

    # connected component
    def equationsPossible3(self, equations: 'List[str]') -> 'bool':
        graph = [[] for i in range(26)]  # adjacent list
        # add edges
        for a, e, _, b in equations:
            if e == '=':
                x, y = ord(a) - ord('a'), ord(b) - ord('a')
                graph[x].append(y)
                graph[y].append(x)
        # find connected component
        color = [None] * 26  # color[i] is the color of node i
        t = -1  # initial color
        for nd in range(26):  # iterates each node
            if color[nd] == None:
                t += 1
                color[nd] = t
                st = [nd]
                while st:
                    nd = st.pop()
                    for nei in graph[nd]:
                        if color[nei] == None:
                            color[nei] = t
                            st.append(nei)

        # find the conflict
        for a, e, _, b in equations:
            if e == '!':
                x = ord(a) - ord('a')
                y = ord(b) - ord('a')
                if color[x] != None and color[y] != None and color[x] == color[y]:
                    return False
        return True

if __name__ == '__main__':
    s = Solution()
    equations=['a==b', 'b==c', 'c==a']
    s.equationsPossible(equations)


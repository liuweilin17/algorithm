###########################################
# Let's Have Some Fun
# File Name: 210.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Feb 12 18:58:13 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#210. Course Schedule II

from collections import defaultdict

class Solution:
    # CLRS dfs solution
    # we sort the node based on finish_time, which is exactly the topological sort
    def findOrder1(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
        start_time = [0] * numCourses
        finish_time = [0] * numCourses
        color = [0] * numCourses # 0:not visit, 1: visit, 2: finish visit
        self.time = 0

        def dfs(numCourses, prerequisites):
            for i in range(numCourses):
                if color[i] == 0:
                    dfs_visit(numCourses, prerequisites, i)

        def dfs_visit(numCourses, prerequisites, i):
            self.time += 1
            start_time[i] = self.time
            color[i] = 1
            for p, q in prerequisites:
                if p == i and color[q] == 0:
                    dfs_visit(numCourses, prerequisites, q)
            self.time += 1
            finish_time[i] = self.time
            color[i] = 2

        dfs(numCourses, prerequisites)
        for i, j in prerequisites:
            if start_time[j]<=start_time[i]<=finish_time[j] and start_time[j]<=finish_time[i]<=finish_time[j]:
                return []
        return sorted(range(numCourses), key=lambda x:finish_time[x])

   # use dfs to find the topological order without finish_time
   # when the node becomes black, then its descendents are black already in topological order.
   # therefore, we simply add the points in the reverse order of coloring black.
   # In the same, in dfs, the order of two white nodes with dfs(i) and dfs(j) in line 72 of iterations does not matter.
    def findOrder2(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
        # build adj_list
        adj_list = defaultdict(list)
        for i, j in prerequisites:
            adj_list[j].append(i)
            
        ret = []
        is_possible = True
        color = [0] * numCourses #0:white, 1:grey, 2:black
        
        def dfs(i):
            nonlocal is_possible
            if not is_possible: return
            color[i] = 1
            for j in adj_list[i]:
                if color[j] == 0:
                    dfs(j)
                elif color[j] == 1: #circle
                    is_possible = False
            color[i] = 2
            ret.append(i)
            
        for i in range(numCourses):
            if color[i] == 0:
                dfs(i)
                
        return ret[::-1] if is_possible else [] 

    # use indegree
    # the node with no indegree should rank first in topological sort
    # then we remove the node along with its edges, the remaining node with no
    # indegree should be the descendents.
    def findOrder3(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'List[int]':
        ret = []
        indegree = {}
        # build adj_list
        adj_list = defaultdict(list)
        for i, j in prerequisites:
            adj_list[j].append(i)
            indegree[i] = indegree.get(i, 0) + 1

        # st stores the 0 indegree nodes
        st = [i for i in range(numCourses) if i not in indegree.keys()]
        while st:
            x = st.pop()
            ret.append(x)
            if x not in adj_list.keys(): continue
            for i in adj_list[x]:
                indegree[i] -= 1
                if indegree[i] == 0:
                    st.append(i)
        return ret if len(ret) == numCourses else []

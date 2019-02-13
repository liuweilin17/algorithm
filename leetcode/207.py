###########################################
# Let's Have Some Fun
# File Name: 207.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Feb 12 18:37:01 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#207. Course Schedule

class Solution:
    # this is based on dfs in CLRS 3rd edition, actually start_time and finish_time is redundant
    def canFinish1(self, numCourses: 'int', prerequisites: 'List[List[int]]') -> 'bool':
        # circle detection with DFS
        start_time = [0] * numCourses
        finish_time = [0] * numCourses
        color = [0] * numCourses # 0:not visit, 1:in visit, 2: end visit
        self.time = 0

        def dfs(prerequisites, numCourses):
            for i in range(numCourses):
                if color[i] == 0:
                    dfs_visit(prerequisites, numCourses, i)

        def dfs_visit(prerequisites, numCourses, i):
            self.time += 1
            start_time[i] = self.time
            color[i] = 1
            for p, q in prerequisites:
                if p == i and color[q] == 0:
                    dfs_visit(prerequisites, numCourses, q)
            self.time += 1
            finish_time[i] = self.time
            color[i] = 2

        dfs(prerequisites, numCourses)
        for i, j in prerequisites:
                if start_time[j] <= start_time[i] <= finish_time[j] and \
                start_time[j] <= finish_time[i] <= finish_time[j]:
                    return False
        return True

    # There is another two methods, which could be seen in question 207.
    # in 207, we simply return [] when it's False

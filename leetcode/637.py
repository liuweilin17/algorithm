###########################################
# Let's Have Some Fun
# File Name: 637.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Jan 23 11:50:27 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 637. Average of Levels in Binary Tree

from queue import Queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # BFS
    def averageOfLevels1(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ret = []
        if not root: return None
        Q = Queue()
        Q.put(root)
        while not Q.empty():
            count = Q.qsize()
            tmp = []
            for i in range(count):
                nd = Q.get()
                tmp.append(nd.val)
                if nd.left: Q.put(nd.left)
                if nd.right: Q.put(nd.right)
            ret.append(sum(tmp) / count)
        return ret

    # DFS
    # we could use DFS, in each step, we could the number and sum of the current level
    def averageOfLevels2(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        def dfs(nd, level, count, summ):
            count[level] = count.get(level, 0) + 1
            summ[level] = summ.get(level, 0) + nd.val
            if nd.left: dfs(nd.left, level+1, count, summ)
            if nd.right: dfs(nd.right, level+1, count, summ)

        count = {}
        summ = {}
        dfs(root, 0, count, summ)
        ret = []
        for i in range(len(count.keys())):
            ret.append(summ[i]/count[i])

        return ret


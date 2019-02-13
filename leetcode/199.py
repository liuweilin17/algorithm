###########################################
# Let's Have Some Fun
# File Name: 199.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Feb 12 15:35:21 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#199. Binary Tree Right Side View

from queue import Queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rightSideView1(self, root: 'TreeNode') -> 'List[int]':
        if not root: return []

        ret = []
        Q = Queue()
        Q.put(root)
        while not Q.empty():
            n = Q.qsize()
            for i in range(n):
                nd = Q.get()
                if nd.left: Q.put(nd.left)
                if nd.right: Q.put(nd.right)
            ret.append(nd.val)
        return ret

    # DFS, I did not come up with this on my own.
    # we use dfs to calculate the depth of each node, but always right first.
    # In this way, we find the rightmost node of each depth.
    def rightSideView2(self, root: 'TreeNode') -> 'List[int]':
        ret = []
        def dfs(root, depth):
            if not root: return
            if depth == len(ret):
                ret.append(root.val)
            dfs(root.right, depth+1)
            dfs(root.left, depth+1)
        dfs(root, 0)
        return ret

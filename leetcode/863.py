###########################################
# Let's Have Some Fun
# File Name: 863.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu 27 Jun 19:45:46 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#863. All Nodes Distance K in Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK1(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.ret = []

        # find the parents of all nodes
        par = {}
        def dfs(nd, parent):
            if not nd: return
            par[nd] = parent
            if nd.left:
                dfs(nd.left, nd)
            if nd.right:
                dfs(nd.right, nd)
        dfs(root, None)

        # bfs in the graph
        queue = [(target, 0)]
        seen = []
        while queue:
            nd, dist = queue.pop(0)
            seen.append(nd)
            if dist == K:
                self.ret.append(nd.val)
            for nei in [nd.left, nd.right, par[nd]]:
                if nei and nei not in seen:
                    queue.append((nei, dist+1))

        return self.ret
    
    def distanceK2(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        self.ret = []

        def dfs(nd): # find the distance(number of nodes) to target from nd
            if not nd: return -1
            if nd is target:
                find_subtree(nd, 0)
                return 1 #Notice return 1 instead of 0
            else:
                L = dfs(nd.left)
                R = dfs(nd.right)
                if L != -1:
                    if L == K: self.ret.append(nd.val)
                    find_subtree(nd.right, L+1)
                    return L+1
                elif R != -1:
                    if R == K: self.ret.append(nd.val)
                    find_subtree(nd.left, R+1)
                    return R+1
                else: return -1

        def find_subtree(nd, depth): # find the nodes with depth in nd subtree
            if not nd: return
            if depth == K:
                self.ret.append(nd.val)
            if nd.left:
                find_subtree(nd.left, depth+1)
            if nd.right:
                find_subtree(nd.right, depth+1)

        dfs(root)

        return self.ret

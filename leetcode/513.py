###########################################
# Let's Have Some Fun
# File Name: 513.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu 20 Jun 10:02:17 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 513. Find Bottom Left Tree Value

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Right to left BFS
    # Notice we could use pop(0) in array to implement queue 
    def findBottomLeftValue(self, root: TreeNode) -> int:
        ret = 0
        queue = [root]
        while queue:
            nd = queue.pop(0)
            ret = nd.val
            if nd.right:
                queue.append(nd.right)
            if nd.left:
                queue.append(nd.left)
                
        return ret

    # in preorder, the leftmost node is the first one to be visited in its layer
    def findBottomLeftValue(self, root: TreeNode) -> int:
        if not root: return 0
        # dfs
        self.ret = 0
        self.dfs = -1
        def dfs(nd, depth):
            if nd:
                if not nd.left and not nd.right:
                    if depth > self.dfs:
                        self.dfs = depth
                        self.ret = nd.val
                dfs(nd.left, depth+1)
                dfs(nd.right, depth+1)
        dfs(root, 0)

        return self.ret

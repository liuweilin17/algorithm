###########################################
# Let's Have Some Fun
# File Name: 111.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat 15 Jun 13:10:26 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 111. Minimum Depth of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # notice we could not simply replate max with min in depth cal to implement minDepth
    def minDepth(self, root: TreeNode) -> int:
        self.min_depth = float('inf')

        def helper(nd, length):
            if not nd.left and not nd.right:
                self.min_depth = min(self.min_depth, length)
            if nd.left and length + 1 < self.min_depth:
                helper(nd.left, length+1)
            if nd.right and length + 1 < self.min_depth:
                helper(nd.right, length+1)

        if not root: return 0
        helper(root, 1)

        return self.min_depth


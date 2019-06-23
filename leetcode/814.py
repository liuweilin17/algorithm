###########################################
# Let's Have Some Fun
# File Name: 814.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon 17 Jun 21:38:58 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#814. Binary Tree Pruning

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def pruneTree(self, root: TreeNode) -> TreeNode:
        if not root: return None

        root.left = self.pruneTree(root.left)
        root.right = self.pruneTree(root.right)

        if root.val == 0 and not root.left and not root.right:
            return None

        return root


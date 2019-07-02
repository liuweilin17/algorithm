###########################################
# Let's Have Some Fun
# File Name: 971.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon  1 Jul 15:34:52 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#971. Flip Binary Tree To Match Preorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def flipMatchVoyage(self, root: TreeNode, voyage: List[int]) -> List[int]:
        self.i = 0
        self.ret = []
        def dfs(node):
            if not node: return
            if node.val != voyage[self.i]:
                self.ret = [-1]
                return
            elif node.left and node.left.val != voyage[self.i + 1]:
                # flip
                self.i += 1
                self.ret.append(node.val)
                dfs(node.right)
                dfs(node.left)
            else:
                self.i += 1
                dfs(node.left)
                dfs(node.right)

        dfs(root)
        return self.ret









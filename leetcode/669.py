###########################################
# Let's Have Some Fun
# File Name: 669.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue  4 Jun 18:39:24 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#669. Trim a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None
        if L <= root.val <= R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
            return root
        elif root.val < L:
            return self.trimBST(root.right, L, R)
        else:
            return self.trimBST(root.left, L, R)


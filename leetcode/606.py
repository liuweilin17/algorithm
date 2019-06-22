###########################################
# Let's Have Some Fun
# File Name: 606.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed  5 Jun 09:55:27 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#606. Construct String from Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def tree2str(self, t: TreeNode) -> str:
        if not t:
            return ''
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)
        if left == '':
            if right != '':
                left = '()'
                right = '(' + right + ')'
        else:
            left = '(' + left + ')'
            if right != '':
                right = '(' + right + ')'

        return str(t.val) + left + right




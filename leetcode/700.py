###########################################
# Let's Have Some Fun
# File Name: 700.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Jan 17 20:48:39 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        ret = None
        if root.val == val:
            ret = root
        elif root.val > val and root.left:
            ret = self.searchBST(root.left, val)
        elif root.val < val and root.right:
            ret = self.searchBST(root.right, val)
        return ret

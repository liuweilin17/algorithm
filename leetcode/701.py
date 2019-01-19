###########################################
# Let's Have Some Fun
# File Name: 701.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Jan 18 20:23:10 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 701. Insert into a Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        def insertIntoBSTRec(nd, val):
            if val < nd.val:
                if nd.left:
                    insertIntoBSTRec(nd.left, val)
                else:
                    nd.left = TreeNode(val)
            else:
                if nd.right:
                    insertIntoBSTRec(nd.right, val)
                else:
                    nd.right = TreeNode(val)

        if not root:
            return TreeNode(val)

        insertIntoBSTRec(root, val)

        return root




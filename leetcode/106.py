###########################################
# Let's Have Some Fun
# File Name: 106.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Feb 11 21:06:01 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#106. Construct Binary Tree from Inorder and Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder: 'List[int]', postorder: 'List[int]') -> 'TreeNode':
        if not inorder or not postorder: return None

        root = TreeNode(postorder[-1])
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                break

        root.left = self.buildTree(inorder[:i], postorder[:i])
        root.right = self.buildTree(inorder[i+1:], postorder[i:-1])
        return root

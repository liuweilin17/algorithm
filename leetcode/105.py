###########################################
# Let's Have Some Fun
# File Name: 105.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Feb 11 20:52:29 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#105. Construct Binary Tree from Preorder and Inorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        if not preorder or not inorder: return None

        root = TreeNode(preorder[0])
        pos = 0
        for i in range(len(inorder)):
            if inorder[i] == root.val:
                pos = i
                break
        if root:
            root.left = self.buildTree(preorder[1:i+1], inorder[:i])
            root.right = self.buildTree(preorder[i+1:], inorder[i+1:])
        return root

    # less memory and less time
    def buildTree1(self, preorder: 'List[int]', inorder: 'List[int]') -> 'TreeNode':
        def helper(pre_start, pre_end, in_start, in_end):
            if pre_start >= pre_end or in_start >= in_end:
                return None
            root = TreeNode(preorder[pre_start])
            for i in range(in_start, in_end):
                if inorder[i] == root.val:
                    break
            root.left = helper(pre_start+1, pre_start+i-in_start+1, in_start, i)
            root.right= helper(pre_start+i-in_start+1, pre_end, i+1, in_end)
            return root

        return helper(0, len(preorder), 0, len(inorder))


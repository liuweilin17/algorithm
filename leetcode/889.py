###########################################
# Let's Have Some Fun
# File Name: 889.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue 18 Jun 19:46:19 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#889. Construct Binary Tree from Preorder and Postorder Traversal

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Notice that given preorder and postorder traversals, there could be multiple trees.
    # Since the question us to find only one of them, then we could use a simpler solution
    def constructFromPrePost(self, pre: List[int], post: List[int]) -> TreeNode:
        N = len(pre)
        if N == 0:
            return None
        root = TreeNode(pre[0])
        if N == 1:
            return root

        v = post[-2]
        k1 = 0 # the root of the right subtree
        for i in range(1, N):
            if pre[i] == v:
                k1 = i
                break

        root.left = self.constructFromPrePost(pre[1:k1], post[:k1-1])
        root.right = self.constructFromPrePost(pre[k1:], post[k1-1:-1])
        return root




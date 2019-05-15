###########################################
# Let's Have Some Fun
# File Name: 543.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon 13 May 14:02:26 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#543. Diameter of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Notice the longest path does not necessarily passes the root !!!
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root: return 0
        self.ret = 0

        def getDepth(nd):
            if not nd: return 0
            L = getDepth(nd.left)
            R = getDepth(nd.right)

            # This is the new line added to update the diameter
            self.ret = max(self.ret, L + R)

            return max(L, R) + 1

        getDepth(root)
        return self.ret


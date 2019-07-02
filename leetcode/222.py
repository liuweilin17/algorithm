###########################################
# Let's Have Some Fun
# File Name: 222.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon  1 Jul 20:01:08 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#222. Count Complete Tree Nodes

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # O(logn * logn)
    # T(n) = T(n/2) + log(n)
    # T(n) = T(n/4) + (logn - 1) + log(n)
    # T(n) = T(n/8) + (logn - 2) + (logn - 1) + log(n)
    # T(n) = T(n/n) + (logn - sqrt(n) + 1) + ... + log(n)
    # T(n) = logn * (sqrt(n) - 1)
    def countNodes(self, root: TreeNode) -> int:
        if not root: return 0
        left_height, right_height = -1, -1
        p = root
        while p:
            left_height += 1
            p = p.left
        p = root
        while p:
            right_height += 1
            p = p.right

        if left_height == right_height: return 2**(left_height+1) - 1
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)



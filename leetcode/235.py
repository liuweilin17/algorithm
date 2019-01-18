###########################################
# Let's Have Some Fun
# File Name: 235.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Jan 17 22:07:18 2019
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
    # recursive method
    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor1(root.right, p, q)
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor1(root.left, p, q)
        else:  # root == q or root == p or min(p,q)<root<min(p,q)
            return root

    # iterative method
    def lowerstCommonAncestor2(self, root, p, q):
        nd = root
        while nd:
            if p.val > nd.val and q.val > nd.val:
                nd = nd.right
            elif p.val < nd.val and q.val < nd.val:
                nd = nd.left
            else:
                return nd


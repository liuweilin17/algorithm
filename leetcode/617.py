###########################################
# Let's Have Some Fun
# File Name: 617.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat 11 May 16:44:21 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#617. Merge Two Binary Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive method
    def mergeTrees1(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1:
            return t2
        if not t2:
            return t1
        root = TreeNode(t1.val + t2.val)
        root.left = self.mergeTrees(t1.left, t2.left)
        root.right = self.mergeTrees(t1.right, t2.right)
        return root

    # iterative method: pre-order traverse of t1
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1: return t2

        st = []
        st.append((t1, t2))
        while st:
            n1, n2 = st.pop()
            if n1 == None or n2 == None:
                continue
            n1.val += n2.val
            if n1.left:
                st.append((n1.left, n2.left))
            else:
                n1.left = n2.left

            if n1.right:
                st.append((n1.right, n2.right))
            else:
                n1.right = n2.right

        return t1

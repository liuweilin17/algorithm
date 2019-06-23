###########################################
# Let's Have Some Fun
# File Name: 897.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue  4 Jun 17:59:03 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#897. Increasing Order Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    #in-order: left,root,right
    def increasingBST1(self, root: TreeNode) -> TreeNode:
        head = TreeNode(-1)
        p = head
        st = []
        nd = root
        while len(st) or nd:
            while nd:
                st.append(nd)
                nd = nd.left
            nd = st.pop()
            bak = nd
            nd = nd.right

            bak.left = None
            bak.right = None
            p.right = bak
            p = bak

        return head.right

    # recursion
    def increasingBST2(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        leftTree = self.increasingBST(root.left)
        rightTree = self.increasingBST(root.right)
        if leftTree:
            head = leftTree
            while leftTree.right:
                leftTree = leftTree.right
            root.left = None
            root.right = rightTree
            leftTree.right = root
            return head
        else:
            root.right = rightTree
            return root


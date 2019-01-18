###########################################
# Let's Have Some Fun
# File Name: 538.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Jan 17 21:05:17 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 538. Convert BST to Greater Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # right->root->left traverse
    def convertBST(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root: return None
        st = []
        nd = root
        sValue = 0
        while len(st) or nd:
            while nd:
                st.append(nd)
                nd = nd.right
            nd = st.pop()
            tmp = nd.val
            nd.val += sValue
            sValue += tmp
            nd = nd.left
        return root


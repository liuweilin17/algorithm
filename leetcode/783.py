###########################################
# Let's Have Some Fun
# File Name: 783.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Jan 17 21:12:15 2019
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
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        minDiff = float('inf')
        pre = None

        st = []
        nd = root
        while len(st) or nd:
            while nd:
                st.append(nd)
                nd = nd.left
            nd = st.pop()
            if pre != None:
                if nd.val - pre < minDiff:
                    minDiff = nd.val - pre
            pre = nd.val
            nd = nd.right
        return minDiff


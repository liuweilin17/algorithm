###########################################
# Let's Have Some Fun
# File Name: 230.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Jan 17 15:59:12 2019
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
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        if not root: return None
        st = []
        nd = root
        n = 0
        while len(st) or nd:
            while nd:
                st.append(nd)
                nd = nd.left
            nd = st.pop()
            if n == k-1:
                return nd.val
            n += 1
            nd = nd.right
        return None

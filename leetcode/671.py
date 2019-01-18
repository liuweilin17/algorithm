###########################################
# Let's Have Some Fun
# File Name: 671.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Jan 17 20:42:20 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 671. Second Minimum Node In a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # brutal method
    def findSecondMinimumValue1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(nd):
            if nd:
                s.add(nd.val)
                dfs(nd.left)
                dfs(nd.right)
        s = set()
        dfs(root)
        ret = float('inf')
        for v in s:
            if v > root.val and v < ret:
                ret = v
        if ret < float('inf'):
            return ret
        else:
            return -1

    # when nd.val > root.val, we need not to check the subtree of nd
    def findSecondMinimumValue2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.ret = float('inf') # use self, otherwise in dfs() ret is considered to be a new inner variable

        def dfs(nd):
            if nd:
                if nd.val > root.val and nd.val < self.ret:
                    self.ret = nd.val
                elif nd.val == root.val:
                    dfs(nd.left)
                    dfs(nd.right)

        dfs(root)
        if self.ret < float('inf'):
            return self.ret
        else:
            return -1




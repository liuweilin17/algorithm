###########################################
# Let's Have Some Fun
# File Name: 107.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Jan 23 11:32:26 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 107. Binary Tree Level Order Traversal II

from queue import Queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if not root: return ret
        Q = Queue()
        Q.put(root)
        while not Q.empty():
            count = Q.qsize()
            tmp = []
            for i in range(count):
                nd = Q.get()
                tmp.append(nd.val)
                if nd.left:
                    Q.put(nd.left)
                if nd.right:
                    Q.put(nd.right)
            ret.append(tmp[:])

        return list(reversed(ret))


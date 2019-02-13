###########################################
# Let's Have Some Fun
# File Name: 116.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Feb 12 14:19:30 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#116. Populating Next Right Pointers in Each Node

import Queue
# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        # bfs
        if not root: return
        Q = Queue.Queue()
        Q.put(root)
        while not Q.empty():
            n = Q.qsize()
            pre = None
            for i in range(n):
                nd = Q.get()
                if pre:
                    pre.next = nd
                pre = nd
                if nd.left:
                    Q.put(nd.left)
                if nd.right:
                    Q.put(nd.right)
            nd.next = None


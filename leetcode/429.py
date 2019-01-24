###########################################
# Let's Have Some Fun
# File Name: 429.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Jan 23 11:55:39 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 429. N-ary Tree Level Order Traversal

from queue import Queue

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return []
        ret = []
        Q = Queue()
        Q.put(root)
        while not Q.empty():
            count = Q.qsize()
            tmp = []
            for i in range(count):
                nd = Q.get()
                tmp.append(nd.val)
                for ch in nd.children:
                    if ch: Q.put(ch)
            ret.append(tmp[:])
        return ret


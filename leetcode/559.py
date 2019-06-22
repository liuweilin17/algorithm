###########################################
# Let's Have Some Fun
# File Name: 559.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue  4 Jun 14:51:46 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#559. Maximum Depth of N-ary Tree

"""
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children
"""
class Solution:
    def maxDepthi1(self, root: 'Node') -> int:
        if not root: return 0
        depth = 1 # Notice the initial value is 1 instead of 0 since root is not None
        for nd in root.children:
            depth = max(self.maxDepth(nd)+1, depth)
        return depth

    def maxDepth2(self, root: 'Node') -> int:
        if not root: return 0
        depth = 0
        for nd in root.children:
            depth = max(self.maxDepth(nd), depth)
        return depth+1
        

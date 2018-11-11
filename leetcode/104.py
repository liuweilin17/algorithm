###########################################
# Let's Have Some Fun
# File Name: 104.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Nov 11 13:44:35 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 104. Maximum Depth of Binary Tree

from basics.Tree import *
import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    # Simple solution: recursive methods
    def maxDepth1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            h1 = self.maxDepth1(root.left)
            h2 = self.maxDepth1(root.right)
            return max(h1, h2) + 1

    # count max depth with BFS
    def maxDepth2(self, root):
        q = queue.Queue()
        if root == None:
            return 0
        q.put(root)
        count = 1 # record the number of nodes in each layer in the tree
        depth = 0 # increment one when all the nodes of a layer is traversed
        while not q.empty():
            nd = q.get()
            count -= 1
            if nd.left:
                q.put(nd.left)
            if nd.right:
                q.put(nd.right)
            if count == 0:
                count = q.qsize()
                depth += 1
        return depth

if __name__ == '__main__':
    a = [3,9,20,'null','null',15,7]
    t = BinaryTree(a)
    r = t.getRoot()
    s = Solution()
    print(s.maxDepth1(r))
    print(s.maxDepth2(r))

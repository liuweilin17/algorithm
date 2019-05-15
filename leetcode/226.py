###########################################
# Let's Have Some Fun
# File Name: 226.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat 11 May 19:55:51 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#226. Invert Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive method
    def invertTree1(self, root: TreeNode) -> TreeNode:
        if not root: return None

        t1 = self.invertTree(root.left)
        t2 = self.invertTree(root.right)
        root.left = t2
        root.right = t1

        return root

    # iterative method, bfs 
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root: return None

        q = Queue()
        q.put(root)
        while not q.empty():
            nd = q.get()
            tmp = nd.right
            nd.right = nd.left
            nd.left = tmp
            if nd.left:
                q.put(nd.left)
            if nd.right:
                q.put(nd.right)

        return root

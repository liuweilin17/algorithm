###########################################
# Let's Have Some Fun
# File Name: 623.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun 30 Jun 10:42:53 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#623. Add One Row to Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # the key is to find the node in depth d-1
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        # BFS
        if d == 1:
            new_root = TreeNode(v)
            new_root.left = root
            return new_root
        else:
            queue = [root]
            depth = 1
            while queue:
                if depth == d-1:
                    break
                N = len(queue)
                for i in range(N):
                    nd = queue.pop(0)
                    if nd.left:
                        queue.append(nd.left)
                    if nd.right:
                        queue.append(nd.right)
                depth += 1

            N = len(queue)
            for i in range(N):
                nd = queue[i]
                bak1 = nd.left
                bak2 = nd.right
                nd.left = TreeNode(v)
                nd.right = TreeNode(v)
                nd.left.left = bak1
                nd.right.right = bak2
            return root


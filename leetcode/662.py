###########################################
# Let's Have Some Fun
# File Name: 662.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon  1 Jul 18:52:36 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#662. Maximum Width of Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # learn to use 2*i, 2*i+1 is really import!!!

    #BFS
    def widthOfBinaryTree1(self, root: TreeNode) -> int:
        ret = 0
        cur_depth = -1
        begin = 0
        queue = [(root, 0, 1)] # node, depth, index
        while queue:
            nd, depth, ind = queue.pop(0)
            if nd:
                queue.append((nd.left, depth+1, 2*ind))
                queue.append((nd.right, depth+1, 2*ind+1))
                if depth != cur_depth:
                    cur_depth = depth
                    begin = ind
                ret = max(ind - begin + 1, ret)

        return ret

    #DFS
    def widthOfBinaryTree2(self, root: TreeNode) -> int:
        self.ret = 0
        begin = {} # the position of the first not none node
        def dfs(nd, depth, pos):
            if nd:
                if depth not in begin: begin[depth] = pos
                self.ret = max(self.ret, pos-begin[depth]+1)
                dfs(nd.left, depth+1, 2*pos)
                dfs(nd.right, depth+1, 2*pos+1)

        dfs(root, 0, 1)
        return self.ret




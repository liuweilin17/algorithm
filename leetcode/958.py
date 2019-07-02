###########################################
# Let's Have Some Fun
# File Name: 958.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu 27 Jun 23:46:48 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#958. Check Completeness of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isCompleteTree1(self, root: TreeNode) -> bool:
        if not root: return False

        queue = [root]
        flag1 = False # whether the last level has been encountered
        while queue:
            N = len(queue)
            flag2 = False # whether None is encountered in this level
            flag3 = False # whether there is not None of next level
            for i in range(N):
                nd = queue.pop(0)
                if nd == None:
                    flag2 = True
                    queue.append(None)
                else:
                    if flag2:
                        return False
                    if nd.left or nd.right: flag3 = True
                    queue.append(nd.left)
                    queue.append(nd.right)
            if flag2:
                if flag1: return False
                else: flag1 = True
            if not flag3: break

        return True

    def isCompleteTree2(self, root: TreeNode) -> bool:
        if not root: return False
        
        # use bfs and calcuate based on v = 2*i + 1, v = 2*i + 2, to see whether 
        # the last index is the same as the number of all nodes
        i = 0
        queue = [(root, 1)]
        while i < len(queue):
            nd, ind = queue[i]
            if nd:
                queue.append((nd.left, 2*ind))
                queue.append((nd.right, 2*ind+1))
            i += 1
            
        return queue[-1][1] == len(queue) # whether there is empty nd in the whole process


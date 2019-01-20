###########################################
# Let's Have Some Fun
# File Name: 95.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Jan 19 19:24:44 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        def generateTreesRec(start, end):
            all_trees = []
            if start > end:
                return [None]
            elif start == end:
                return [TreeNode(start)]
            else:
                for i in range(start, end+1):
                    left = generateTreesRec(start, i-1)
                    right = generateTreesRec(i+1, end)
                    for ln in left:
                        for rn in right:
                            nd = TreeNode(i)
                            nd.left = ln
                            nd.right = rn
                            all_trees.append(nd)
                return all_trees

        if n < 1:
            return []
        else:
            return generateTreesRec(1, n)




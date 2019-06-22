###########################################
# Let's Have Some Fun
# File Name: 572.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat 15 Jun 12:44:03 2019
###########################################
#coding=utf-8
#!/usr/bin/python



# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # notice that equal function is necessary !!!
    # we need make sure sub_s and t is completely equal rather than t is the subtree of sub_s.left or sub_s.right
    # bad case is:
    # s: [3,4,5,1,null,2]
    # t: [3,1,2]

    # recursive method 1
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def traverse(s, t):
            return s != None and (equals(s, t) or traverse(s.left, t) or traverse(s.right, t))

        def equals(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and equals(s.left, t.left) and equals(s.right, t.right)

        return traverse(s, t)

    # recursive method 2
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:

        def equal(s, t):
            if not s and not t:
                return True
            if not s or not t:
                return False
            return s.val == t.val and equal(s.left, t.left) and equal(s.right, t.right)

        return equal(s, t) or (s != None and (self.isSubtree(s.left, t) or self.isSubtree(s.right, t)))

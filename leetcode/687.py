###########################################
# Let's Have Some Fun
# File Name: 687.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon 17 Jun 21:17:09 2019
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
    def longestUnivaluePath(self, root: TreeNode) -> int:
        self.max_len = 0

        # the length of longest path extended from nd
        def maxLen(nd):
            if not nd: return 0
            # Notice the call of maxLen is essential !!!
            left_child_len = maxLen(nd.left)
            right_child_len = maxLen(nd.right)
            left_len, right_len = 0, 0
            if nd.left and nd.left.val == nd.val:
                left_len = left_child_len + 1
            if nd.right and nd.right.val == nd.val:
                right_len = right_child_len + 1

            self.max_len = max(self.max_len, left_len + right_len)

            return max(left_len, right_len)

        maxLen(root)
        return self.max_len


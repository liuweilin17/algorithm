###########################################
# Let's Have Some Fun
# File Name: 337.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed 15 May 10:57:53 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#337. House Robber III

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    dp = {}
    def rob(self, root: TreeNode) -> int:
        if root in self.dp: return self.dp[root]

        if not root: return 0

        v1 = self.rob(root.left) + self.rob(root.right)
        v2 = root.val
        if root.left:
            v2 += self.rob(root.left.left) + self.rob(root.left.right)
        if root.right:
            v2 += self.rob(root.right.left) + self.rob(root.right.right)

        self.dp[root] = max(v1, v2)
        return max(v1, v2)


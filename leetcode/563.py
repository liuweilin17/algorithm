###########################################
# Let's Have Some Fun
# File Name: 563.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat 15 Jun 11:32:49 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 563. Binary Tree Tilt

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.tilt = 0

        def cal_sum(nd):
            if not nd:
                return 0
            left_sum = cal_sum(nd.left)
            right_sum = cal_sum(nd.right)
            self.tilt += abs(left_sum - right_sum)

            return nd.val + left_sum + right_sum

        cal_sum(root)

        return self.tilt


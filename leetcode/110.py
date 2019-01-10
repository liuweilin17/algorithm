###########################################
# Let's Have Some Fun
# File Name: 110.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Jan  9 22:24:43 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 110. Balanced Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # my method, which is easy to understand
    def isBalanced1(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return 0
        return abs(self.getDepth(root.left) - self.getDepth(root.right)) <= 1 and self.isBalanced(root.left) and self.isBalanced(root.right)

    def getDepth(self, node):
        if node == None:
            return 0
        else:
            return max(self.getDepth(node.left), self.getDepth(node.right)) + 1

    # better method, which decide if the tree is balanced in the process of calculating the depth
    def isBalanced2(self, root):
        return self.maxDepth(root) != -1

    def maxDepth(self, node):
        if node == None:
            return 0
        left = self.maxDepth(node.left)
        right = self.maxDepth(node.right)
        if left == -1 or right == -1 or abs(left-right) > 1:
            return -1
        else:
            return max(left, right) + 1

if __name__ == '__main__':
    s = Solution()


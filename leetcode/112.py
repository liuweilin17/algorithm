###########################################
# Let's Have Some Fun
# File Name: 112.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Jan 13 12:25:22 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 112. Path Sum

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # count the sum
    def hasPathSum1(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """
        if not root:
            return False

        st = []
        st.append((root, root.val))
        while len(st):
            nd, t = st.pop()
            if not nd.left and not nd.right:
                if t == sum:
                    return True
            if nd.left:
                st.append((nd.left, t + nd.left.val))
            if nd.right:
                st.append((nd.right, t + nd.right.val))
        return False

    # use substraction, quicker
    def hasPathSum2(self, root, sum):
        if not root:
            return False
        st = []
        st.append((root, sum-root.val))
        while len(st):
            nd, t = st.pop()
            if not nd.left and not nd.right:
                if t == 0:
                    return True
            if nd.left:
                st.append((nd.left, t-nd.left.val))
            if nd.right:
                st.append((nd.right, t-nd.right.val))
        return False

    # use substraction and recursive
    def hasPathSum3(self, root, sum):
        if not root:
            return False
        sum -= root.val
        if not root.left and not root.right:
            if sum == 0:
                return True
        f1 = self.hasPathSum3(root.left, sum) if root.left else False
        f2 = self.hasPathSum3(root.right, sum) if root.right else False
        return f1 or f2


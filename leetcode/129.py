###########################################
# Let's Have Some Fun
# File Name: 129.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Jan 13 20:27:28 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 129. Sum Root to Leaf Numbers

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive method
    def sumNumbers1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def sumNumbersRec(nd, sum, total):
            sum = sum * 10 + nd.val
            if not nd.left and not nd.right:
                total.append(sum)
            if nd.left:
                sumNumbersRec(nd.left, sum, total)
            if nd.right:
                sumNumbersRec(nd.right, sum, total)
        if not root:
            return
        ret = []
        sumNumbersRec(root, 0, ret)
        return sum(ret)

    # Iterative method
    def sumNumbers2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        ret = 0
        st = []
        st.append((root, root.val))
        while len(st):
            nd, sum = st.pop()
            if not nd.left and not nd.right:
                ret += sum
            if nd.left:
                st.append((nd.left, sum * 10 + nd.left.val))
            if nd.right:
                st.append((nd.right, sum * 10 + nd.right.val))
        return ret


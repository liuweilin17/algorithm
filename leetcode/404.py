###########################################
# Let's Have Some Fun
# File Name: 404.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat 15 Jun 11:19:41 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 404. Sum of Left Leaves

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive method
    def sumOfLeftLeaves1(self, root: TreeNode) -> int:
        self.sumV = 0
        def dfs(nd, flag):
            if nd:
                # flag=0 right child, flag=1 left child
                if not nd.left and not nd.right and flag == 1:
                    self.sumV += nd.val

                if nd.left:
                    dfs(nd.left, 1)
                if nd.right:
                    dfs(nd.right, 0)

        dfs(root, -1)
        return self.sumV

    # iterative method
    def sumOfLeftLeaves2(self, root: TreeNode) -> int:
        if not root:
            return 0

        st = []
        st.append((root, -1))
        sumV = 0
        while len(st):
            nd, flag = st.pop()
            if not nd.left and not nd.right and flag == 1:
                sumV += nd.val

            if nd.left:
                st.append((nd.left, 1))
            if nd.right:
                st.append((nd.right, 0))

        return sumV


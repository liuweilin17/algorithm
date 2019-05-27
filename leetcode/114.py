###########################################
# Let's Have Some Fun
# File Name: 114.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun 26 May 19:20:01 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#114. Flatten Binary Tree to Linked List

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive method
    def flatten1(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root:
            self.flatten(root.left)
            self.flatten(root.right)
            p = root.left
            if p:
                while p.right:
                    p = p.right
                p.right = root.right
                root.right = root.left
                root.left = None

    # dfs, pre order
    def flatten2(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        # pre order traverse
        st = [root]
        pre = None
        while st:
            nd = st.pop()
            if pre:
                pre.left = None
                pre.right = nd
            pre = nd
            
            if nd.right:
                st.append(nd.right)
            if nd.left:
                st.append(nd.left)

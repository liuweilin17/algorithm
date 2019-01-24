###########################################
# Let's Have Some Fun
# File Name: 144.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Jan 23 17:54:33 2019
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
    # recursive
    def preorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def dfs(nd, ret):
            if nd:
                ret.append(nd.val)
                if nd.left: dfs(nd.left, ret)
                if nd.right: dfs(nd.right, ret)

        ret = []
        dfs(root, ret)
        return ret

    # iterative
    def preorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        ret = []
        st = []
        st.append(root)
        while len(st):
            nd = st.pop()
            ret.append(nd.val)
            if nd.right: st.append(nd.right)
            if nd.left: st.append(nd.left)
        return ret

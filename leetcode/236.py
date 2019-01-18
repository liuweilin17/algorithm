###########################################
# Let's Have Some Fun
# File Name: 236.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Jan 18 15:54:09 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 236. Lowest Common Ancestor of a Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # recursive method, check p,q existence of subtrees
    def __init__(self):
        self.flag = None

    def lowestCommonAncestor1(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        def traverse(nd):
            if not nd:
                return False

            left = traverse(nd.left)
            right = traverse(nd.right)

            mid = (nd == p or nd == q)

            if left + right + mid > 2:
                self.flag = nd

            return left or right or mid

        traverse(root)
        return self.flag

    # use dfs to record the predecessor of each node
    def lowestCommonAncestor2(self, root, p, q):
        st = []
        dt = {}
        dt[root] = None
        st.append(root)
        while len(st):
            nd = st.pop()
            if nd.left:
                dt[nd.left] = nd
                st.append(nd.left)
            if nd.right:
                dt[nd.right] = nd
                st.append(nd.right)

        predecessors = []
        while p:
            predecessors.append(p)
            p = dt[p]

        while q not in predecessors:
            q = dt[q]

        return q

###########################################
# Let's Have Some Fun
# File Name: 99.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Oct 13 18:07:29 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#99. Recover Binary Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # time: O(N)
    # space: O(h), the height of the tree
    def recoverTree(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # traverse with in-order, left->root->right
        st = []
        nd = root
        a, b, pre = None, None, None
        while st or nd:
            while nd:
                st.append(nd)
                nd = nd.left
            nd = st.pop()
            # process the node
            if pre:
                if nd.val < pre.val:
                    b = nd # b is the smallest one
                    if a == None:
                        a = pre
                    else:
                        break
            pre = nd
            nd = nd.right

        # swap a and b
        tmp = a.val
        a.val = b.val
        b.val = tmp

·

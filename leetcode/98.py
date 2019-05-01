###########################################
# Let's Have Some Fun
# File Name: 98.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Jan 20 13:35:39 2019
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
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        # in order traversal
        if not root: # this is interesting
            return True
        st = []
        nd = root
        pre = None
        while len(st) or nd:
            while nd:
                st.append(nd)
                nd = nd.left
            nd = st.pop()
            if pre != None: # can't use 'if pre', cause pre could be int(0)
                if nd.val <= pre: # notice it should be <= rather than <
                    return False
            pre = nd.val
            nd = nd.right
        return True


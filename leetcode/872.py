###########################################
# Let's Have Some Fun
# File Name: 872.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue  4 Jun 18:17:12 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#872. Leaf-Similar Trees

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getLeaves(self, root):
        ret = []
        if not root:
            return ret
        st = [root]
        while len(st):
            nd = st.pop()
            if not nd.left and not nd.right:
                ret.append(nd.val)
            if nd.right:
                st.append(nd.right)
            if nd.left:
                st.append(nd.left)
        return ret

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        seq1 = self.getLeaves(root1)
        seq2 = self.getLeaves(root2)
        N1, N2 = len(seq1), len(seq2)
        if N1 != N2:
            return False
        else:
            for i in range(N1):
                if seq1[i] != seq2[i]:
                    return False
            return True



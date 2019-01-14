###########################################
# Let's Have Some Fun
# File Name: 437.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Jan 13 14:04:31 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 437. Path Sum III

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive ways
    def pathSum1(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        def pathSumRec(nd, sum, path):
            path.append(nd.val)
            total = 0
            ret = 0
            for i in range(len(path)):
                total += path[-i-1]
                if total == sum:
                    ret += 1
            r1 = pathSumRec(nd.left, sum, path[:]) if nd.left else 0
            r2 = pathSumRec(nd.right, sum, path[:]) if nd.right else 0
            return ret + r1 + r2

        if not root:
            return 0

        return pathSumRec(root, sum, [])

    # Iterative method
    def pathSum2(self, root, sum):
        if not root:
            return 0
        ret = 0
        st = []
        st.append((root, [root.val]))
        while len(st):
            nd, path = st.pop()
            total = 0
            for i in range(len(path)):
                total += path[-i-1]
                if total == sum:
                    ret += 1
            if nd.left:
                tmp = path[:]
                tmp.append(nd.left.val)
                st.append((nd.left, tmp[:]))
            if nd.right:
                tmp = path[:]
                tmp.append(nd.right.val)
                st.append((nd.right, tmp[:]))
        return ret

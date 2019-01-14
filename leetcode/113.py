###########################################
# Let's Have Some Fun
# File Name: 113.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Jan 13 13:30:46 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 113. Path Sum II
# similar questions: 112

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # Recursive method
    def pathSum1(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        def pathSumSub(nd, sum, path, paths):
            path.append(nd.val)
            sum -= nd.val
            if not nd.left and not nd.right:
                if sum == 0:
                    paths.append(path)
            if nd.left:
                pathSumSub(nd.left, sum, path[:], paths)
            if nd.right:
                pathSumSub(nd.right, sum, path[:], paths)
        if not root:
            return []
        paths = []
        pathSumSub(root, sum, [], paths)
        return paths

    # Iterative method
    def pathSum2(self, root, sum):
        if not root:
            return []
        paths = []
        st = []
        st.append((root, [root.val], sum-root.val))
        while len(st):
            nd, path, curSum = st.pop()
            if not nd.left and not nd.right:
                if curSum == 0:
                    paths.append(path[:])
            if nd.left:
                tmp = path[:]
                tmp.append(nd.left.val)
                st.append((nd.left, tmp[:], curSum-nd.left.val))
            if nd.right:
                tmp = path[:]
                tmp.append(nd.right.val)
                st.append((nd.right, tmp[:], curSum-nd.right.val))
        return paths




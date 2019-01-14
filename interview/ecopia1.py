###########################################
# Let's Have Some Fun
# File Name: ecopia1.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Jan 13 20:42:50 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# Ecopia interview question 1
# given a binary tree, find

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

from basics.Tree import *

class Solution:
    # recursive method
    def maxSum1(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def maxSumRec(nd, sum, sums):
            sum += nd.val
            if not nd.left and not nd.right:
                sums.append(sum)
            if nd.left:
                maxSumRec(nd.left, sum, sums)
            if nd.right:
                maxSumRec(nd.right, sum, sums)
        if not root:
            return
        sums = []
        maxSumRec(root, 0, sums)
        return max(sums)

    # Iterative method
    def maxSum2(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        maxV = float('-inf')
        st = []
        st.append((root, root.val))
        while len(st):
            nd, sum = st.pop()
            if not nd.left and not nd.right:
                if sum > maxV:
                    maxV = sum
            if nd.left:
                st.append((nd.left, sum + nd.left.val))
            if nd.right:
                st.append((nd.right, sum + nd.right.val))
        return maxV

if __name__ == '__main__':
    s = Solution()
    a = [3,9,20,'null','null',15,7]
    t = BinaryTree(a)
    print(s.maxSum1(t.root))
    print(s.maxSum2(t.root))


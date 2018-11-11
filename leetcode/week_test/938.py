###########################################
# Let's Have Some Fun
# File Name: 938.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Nov 11 13:14:32 2018
###########################################
#coding=utf-8
#!/usr/bin/python

import queue

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        sum = 0
        q = queue.Queue()
        q.put(root)
        while not q.empty():
            n = q.get()
            v = n.val
            if v >= L and v <= R:
                sum += v
            if n.left != None:
                q.put(n.left)
            if n.right != None:
                q.put(n.right)
        return sum


if __name__ == "__main__":
    s = Solution()

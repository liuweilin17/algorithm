###########################################
# Let's Have Some Fun
# File Name: 102.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Jan 23 11:21:18 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 102. Binary Tree Level Order Traversal

from queue import Queue
from basics.Tree import *

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        ret = []
        if not root: return ret
        Q = Queue()
        Q.put(root)
        while not Q.empty():
            count = Q.qsize()
            tmp = []
            for i in range(count):
                nd = Q.get()
                tmp.append(nd.val)
                if nd.left:
                    Q.put(nd.left)
                if nd.right:
                    Q.put(nd.right)
            ret.append(tmp[:])
        return ret

if __name__ == '__main__':
    s = Solution()
    t = BinaryTree([3,9,20,'null','null',15,7])
    printTreeBFS(t.root)
    print(s.levelOrder(t.root))

###########################################
# Let's Have Some Fun
# File Name: 173.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Jan 19 10:11:09 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 173. Binary Search Tree Iterator

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# simply divide standard inOrder traverse into the three functions
class BSTIterator:

    def __init__(self, root):
        """
        :type root: TreeNode
        """
        self.root = root
        self.st = []
        self.cur = root


    def next(self):
        """
        @return the next smallest number
        :rtype: int
        """
        while self.cur:
            self.st.append(self.cur)
            self.cur = self.cur.left
        cur = self.st.pop()
        self.cur = cur.right
        return cur.val

    def hasNext(self):
        """
        @return whether we have a next smallest number
        :rtype: bool
        """
        if len(self.st) or self.cur:
            return True
        else:
            return False




# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()

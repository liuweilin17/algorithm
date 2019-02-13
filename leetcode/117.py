###########################################
# Let's Have Some Fun
# File Name: 117.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Feb 12 15:30:10 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#117. Populating Next Right Pointers in Each Node II

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    def connect(self, root):
        if not root: return

        while root:
            levelStart = TreeLinkNode(0) # temporary node
            cur = levelStart # node of children level
            while root: # node of parent level
                if root.left:
                    cur.next = root.left
                    cur = cur.next
                if root.right:
                    cur.next = root.right
                    cur = cur.next
                root = root.next
            root = levelStart.next


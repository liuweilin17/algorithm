###########################################
# Let's Have Some Fun
# File Name: 919.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu 20 Jun 23:43:34 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#919. Complete Binary Tree Inserter

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class CBTInserter:

    def __init__(self, root: TreeNode):
        self.root = root

    def insert(self, v: int) -> int:
        queue = [self.root]
        while queue:
            nd = queue.pop(0)
            if nd.left:
                queue.append(nd.left)
            else:
                nd.left = TreeNode(v)
                return nd.val
            if nd.right:
                queue.append(nd.right)
            else:
                nd.right = TreeNode(v)
                return nd.val

    def get_root(self) -> TreeNode:
        return self.root

# we use self.candi to memorize all the node with 0 or 1 children
class CBTInserter1:

    def __init__(self, root: TreeNode):
        self.root = root
        self.candi = []
        st = [root]
        while st:
            nd = st.pop(0)
            if not nd.left or not nd.right:
                self.candi.append(nd)
            if nd.left:
                st.append(nd.left)
            if nd.right:
                st.append(nd.right)


    def insert(self, v: int) -> int:
        nd = self.candi[0]
        new_nd = TreeNode(v)
        self.candi.append(new_nd)
        if not nd.left:
            nd.left = new_nd
        else:
            nd.right = new_nd
            self.candi.pop(0)
        return nd.val

    def get_root(self) -> TreeNode:
        return self.root




###########################################
# Let's Have Some Fun
# File Name: 655.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri 21 Jun 20:44:19 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#655. Print Binary Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def printTree(self, root: TreeNode) -> List[List[str]]:
        # calculate height and width of the matrix
        def get_height(nd):
            if not nd: return 0
            return 1 + max(get_height(nd.left), get_height(nd.right))

        def update(nd, row, left, right):
            if not nd: return
            mid = (left + right) // 2
            ret[row][mid] = str(nd.val)
            update(nd.left, row+1, left, mid-1)
            update(nd.right, row+1, mid+1, right)

        height = get_height(root)
        width = 2 ** height - 1 # this is essential

        ret = [[''] * width for _ in range(height)]
        update(root, 0, 0, width-1)

        return ret


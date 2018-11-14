###########################################
# Let's Have Some Fun
# File Name: 108.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Nov 14 11:43:36 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 108. Convert Sorted Array to Binary Search Tree


from basics.Tree import *
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        l = len(nums)
        mid = int(l / 2)
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid+1:])
        return root


if __name__ == '__main__':
    s = Solution()
    a = [-10, -3, 0, 5, 9]
    root = s.sortedArrayToBST(a)
    printTree(root)

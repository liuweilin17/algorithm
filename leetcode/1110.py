###########################################
# Let's Have Some Fun
# File Name: 1110.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun  7 Jul 11:52:22 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#1110. Delete Nodes And Return Forest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # the key is: root is added when it has no parent and not delete !!!
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        to_delete_set = set(to_delete)
        ret = []
        def helper(root, is_root):
            if not root: return None
            deleted = root.val in to_delete_set
            if is_root and not deleted:
                ret.append(root)
            root.left = helper(root.left, deleted)
            root.right = helper(root.right, deleted)
            return root if not deleted else None
        helper(root, True)
        return ret



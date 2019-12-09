###########################################
# Let's Have Some Fun
# File Name: 297.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Dec  8 18:38:09 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#297. Serialize and Deserialize Binary Tree

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        # we add 'None' to store the structure of the tree
        serial = ""
        def helper(nd):
            if nd == None:
                return 'None,'
            return str(nd.val) + ',' + helper(nd.left) + helper(nd.right)
        return helper(root)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        lst = data.split(',')
        def helper(lst):
            if lst[0] == 'None':
                lst.pop(0)
                return None
            root = TreeNode(lst[0])
            lst.pop(0)
            root.left = helper(lst)
            root.right = helper(lst)
            return root
        return helper(lst)



# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

###########################################
# Let's Have Some Fun
# File Name: 449.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Jan 19 11:02:43 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 449. Serialize and Deserialize BST

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
        # ret stores the preOrder traversal
        if not root: return ''

        ret = []
        st = []
        st.append(root)
        while len(st):
            nd = st.pop()
            ret.append(str(nd.val))
            if nd.right:
                st.append(nd.right)
            if nd.left:
                st.append(nd.left)
        return ','.join(ret)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        dataArr = data.split(',')
        l = len(dataArr)
        if l < 1:
            return None
        if dataArr[0] == '':
            return None

        r = int(dataArr[0])
        root = TreeNode(r)
        ls = ''
        rs = ''
        for i in range(1, l):
            if int(dataArr[i]) < r:
                ls += dataArr[i]
            else:
                rs += dataArr[i]

        root.left = self.deserialize(ls)
        root.right = self.deserialize(rs)

        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

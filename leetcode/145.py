###########################################
# Let's Have Some Fun
# File Name: 145.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Jan 23 13:05:44 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

# 145. Binary Tree Postorder Traversal

class Solution:
    # iterative1
    def postorderTraversal1(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        ret = []
        st = []
        nd = root
        pre = None
        while len(st) or nd:
            while nd:
                st.append(nd)
                nd = nd.left

            nd = st[-1] # we need to check if we could traverse nd
            if pre and pre == nd.right: # right child has been visited
                ret.append(nd.val)
                st.pop()
                pre = nd
                nd = None # notice!!!, other wise nd's left children will be put into stack again.
            else:
                if not nd.right: # no right child
                    ret.append(nd.val)
                    st.pop()
                    pre = nd
                nd = nd.right # try to visit right child

        return ret
    
    # iterative2
    # new preorder root->right->left, and reverse the results
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root: return []
        ret = []
        st = []
        st.append(root)
        while len(st):
            nd = st.pop()
            ret.append(nd.val)
            if nd.left:
                st.append(nd.left)
            if nd.right:
                st.append(nd.right)
        return list(reversed(ret))




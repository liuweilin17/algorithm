###########################################
# Let's Have Some Fun
# File Name: 101.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Nov 13 15:49:20 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 101. Symmetric Tree

from basics.Tree import *
import queue
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

	# use BFS
	# if the nodes are symmetrix in each layer, then it is symmetric
	# notice, the None node should be considered
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = queue.Queue()
        if root == None:
            return True
        else:
            q.put(root)
            count = 1
            nd_list = []
            while not q.empty():
                nd = q.get()
                count -= 1
                nd_list.append(nd)
                if nd:
                    q.put(nd.left)
                    q.put(nd.right)
                if count == 0:
                    l = len(nd_list)
                    mid = int((l - 1) / 2)
                    for i in range(0, mid+1):
                        if nd_list[i] != None and nd_list[l-1-i] != None:
                            if nd_list[i].val != nd_list[l-1-i].val:
                                return False
                        elif nd_list[i] == None and nd_list[l-1-i] == None:
                            pass
                        else:
                            return False
                    count = q.qsize()
                    nd_list = []
        return True

    # use recursive ways
    # if a tree is sysmetrix, then its left tree is equal to its right tree
    def isSymmetric1(self, root):
        return self.isMirror(root, root)

    def isMirror(self, t1, t2):
        if t1 == None and t2 == None:
            return True
        elif t1 != None and t2 != None:
            return t1.val == t2.val and self.isMirror(t1.left, t2.right) and self.isMirror(t1.right, t2.left)
        else:
            return False

if __name__ == '__main__':
    s = Solution()
    T1 = BinaryTree([1,2,2,3,4,4,3])
    T2 = BinaryTree([1,2,2,'null',3,'null',3])
    print(s.isSymmetric(T1.root))
    print(s.isSymmetric1(T1.root))
    print(s.isSymmetric(T2.root))
    print(s.isSymmetric1(T2.root))

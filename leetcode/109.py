###########################################
# Let's Have Some Fun
# File Name: 109.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Jan 19 23:04:32 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    # transfer linkedlist to array, and then make the tree
    def sortedListToBST1(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def arrayToBST(ls):
            l = len(ls)
            if len(ls) < 1:
                return None
            mid = (l-1)//2
            nd = TreeNode(ls[mid])
            nd.left = arrayToBST(ls[0:mid])
            nd.right = arrayToBST(ls[mid+1:l])
            return nd


        ls = []
        while head:
            ls.append(head.val)
            head = head.next

        return arrayToBST(ls)

    # This method directly uses the linkedlist
    def sortedListToBST2(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        def getMid(hd):
            prePT = None
            slowPT = hd
            fastPT = hd
            while fastPT and fastPT.next:
                prePT = slowPT
                slowPT = slowPT.next
                fastPT = fastPT.next.next
            if prePT:
                prePT.next = None
            return slowPT
        
        if not head: return None
        mid = getMid(head)
        nd = TreeNode(mid.val)
        if mid == head:
            return nd
        nd.left = self.sortedListToBST(head)
        nd.right = self.sortedListToBST(mid.next)
        return nd
        

###########################################
# Let's Have Some Fun
# File Name: 61.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Jan 21 18:33:34 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 61. Rotate List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head: return None

        p = head
        n = 1 # number of nodes in the linkedlist
        while p.next:
            n += 1
            p = p.next
        p.next = head # make a recurrent linkedlist
        k = n - k % n
        p = head
        for i in range(k-1):
            p = p.next
        ret = p.next
        p.next = None
        return ret





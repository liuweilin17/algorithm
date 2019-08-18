###########################################
# Let's Have Some Fun
# File Name: 82.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri 16 Aug 10:27:33 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 82. Remove Duplicates from Sorted List II

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        # empty head pointer
        h = ListNode(0)
        h.next = head
        p = h
        while p and p.next and p.next.next:
            q = p.next
            r = q.next
            if q.val == r.val:
                v = q.val
                while q and q.val == v:
                    bak = q
                    q = q.next
                    del bak
                p.next = q # Notice this is essential
            else:
                p = q

        return h.next


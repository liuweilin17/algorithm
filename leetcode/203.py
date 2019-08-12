###########################################
# Let's Have Some Fun
# File Name: 203.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue  9 Jul 19:19:15 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#203. Remove Linked List Elements

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements1(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        p, q = new_head, head
        while q:
            if q.val == val:
                p.next = q.next
                del q
                q = p.next
            else:
                p = q
                q = q.next
        return new_head.next

    def removeElements2(self, head: ListNode, val: int) -> ListNode:
        new_head = ListNode(0)
        new_head.next = head
        p = new_head
        while p and p.next:
            if p.next.val == val:
                q = p.next
                p.next = q.next
                del q
            else:
                p = p.next

        return new_head.next



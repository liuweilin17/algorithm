###########################################
# Let's Have Some Fun
# File Name: 148.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan 29 00:42:07 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#148. Sort List

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        def merge(l1, l2):
            if l1 and l2:
                if l1.val < l2.val:
                    l3 = l1
                    l1 = l1.next
                else:
                    l3 = l2
                    l2 = l2.next
                l3.next = None
                ret = l3

                while l1 and l2:
                    if l1.val < l2.val:
                        l3.next = l1
                        l1 = l1.next
                    else:
                        l3.next = l2
                        l2 = l2.next
                    l3 = l3.next
                if l1: l3.next = l1 # no not!!!
                if l2: l3.next = l2 # no not!!!
                return ret

            elif l1:
                return l1
            else:
                return l2

        if not head or not head.next: return head
        # cut the head into two halves
        # pre is necessary, if we use slow to split the list, it will result in untermination.
        # in the case of two nodes in a linked list
        pre, slow, fast = None, head, head
        while slow and fast and fast.next:
            pre = slow
            slow = slow.next
            fast = fast.next.next
        pre.next = None

        l1 = self.sortList(head)
        l2 = self.sortList(slow)
        return merge(l1, l2)

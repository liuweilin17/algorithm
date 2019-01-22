###########################################
# Let's Have Some Fun
# File Name: 328.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Jan 21 13:45:13 2019
###########################################
#coding=utf-8
#!/usr/bin/python

from basics.LinkedList import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    # This is my solution
    # we make two list of even and odd, and then merge
    def oddEvenList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        p1 = head
        p2 = head.next
        bak = head.next # head of even
        while p1 and p2:
            if p1.next:
                if not p1.next.next:
                    break
                p1.next = p1.next.next
                p1 = p1.next
            if p2.next:
                p2.next = p2.next.next
                p2 = p2.next
        if p1:
            p1.next = bak

        return head

    # This the simpler version given in the solution
    def oddEvenList2(self, head):
        if not head:
            return None

        odd = head
        even = head.next
        evenHead = head.next
        while even and even.next:
            odd.next = even.next
            odd = odd.next
            even.next = odd.next
            even = even.next

        odd.next = evenHead

        return head


if __name__ == '__main__':
    s = Solution()
    l = LinkedList([1,2,3,4])
    hd = s.oddEvenList2(l.head)
    #hd = l.head
    while hd:
        print(hd.val)
        hd = hd.next



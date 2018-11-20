###########################################
# Let's Have Some Fun
# File Name: 234.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Nov 19 22:29:44 2018
###########################################
#coding=utf-8
#!/usr/bin/python

#234. Palindrome Linked List

from basics.LinkedList import *

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        # The simpliest way is using stack, while it takes O(n) space
        # We simply reverse the half linkedlist to make it work
        # However, it could change the structure of original linkedlist
        n = 0
        p = head
        while p != None:
            n += 1
            p = p.next
        if n == 0:
            return True
        elif n == 1:
            return True
        elif n % 2 == 0:
            ind = int(n/2)
        else:
            ind = int(n/2) + 1
        h = head
        for i in range(ind):
            h = h.next

        # h is the head of the second half of the linked list
        # reverse list beginning at h
        p = h.next
        h.next = None
        while(p != None):
            q = p.next
            p.next = h
            h = p
            p = q

        p1 = head
        p2 = h
        while(p2 != None):
            if p1.val != p2.val:
                return False
            p1 = p1.next
            p2 = p2.next
        return True


if __name__ == '__main__':
    s = Solution()
    l = LinkedList([1, 2, 4, 2, 1])
    print(s.isPalindrome(l.head))



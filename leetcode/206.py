###########################################
# Let's Have Some Fun
# File Name: 206.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Oct 12 17:12:19 2018
###########################################
#coding=utf-8
#!/usr/bin/python

# 206. Reverse Linked List

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head
        self.size = 0

    def insert(self, val):
        n = ListNode(val)
        n.next = self.head
        self.head = n
        self.size += 1

    def printList(self):
        p = self.head
        while(p):
            print p.val,
            p = p.next

class Solution(object):
    def reverseList1(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        # the head is None or the head is the only node
        if head == None or head.next == None:
            return head

        # p is head pointing None, q is p.next
        p = head
        q = p.next
        p.next = None
       
        # reverse by making q points to p
        r = q.next
        q.next = p
        
        while(r!=None):
            # p,q,r >> 1
            p = q
            q = r
            r = q.next

            #reverse
            q.next = p

        return q

    def reverseList2(self, head: ListNode) -> ListNode:
        ret = None

        # insert each node head ahead of ret
        p = head
        while p:
            q = p.next
            p.next = ret
            ret = p
            p = q

        return ret

    # recursive version
    def reverseList3(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        p = self.reverseList(head.next)
        head.next.next = head
        head.next = None # Notice this is essential
        return p

if __name__ == '__main__':
    ls = LinkedList()
    for i in range(1,6):
        ls.insert(i)
    ls.printList()
    print ''

    s = Solution()
    new_head = s.reverseList(ls.head)
    ls_new = LinkedList(new_head)
    ls_new.printList()

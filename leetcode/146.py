###########################################
# Let's Have Some Fun
# File Name: 146.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue  4 Jun 14:40:36 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#146. LRU Cache

class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.pre = None
        self.next = None

# double linked list and hashtable
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.count = 0
        self.dt = {} # key:value
        self.head = ListNode(0, 0)
        self.tail = self.head

    def get(self, key: int) -> int:
        nd = self.dt.get(key, None)
        if nd != None: # update head
            if nd != self.tail: # move nd to the tail
                nd.pre.next = nd.next
                nd.next.pre = nd.pre
                self.tail.next = nd
                nd.pre = self.tail
                nd.next = None
                self.tail = nd
            return nd.val
        else:
            return -1


    def put(self, key: int, value: int) -> None:
        val = self.get(key)
        if val != -1: # previous get function already move nd to tail
            self.tail.val = value
        elif self.count >= self.capacity:
            tmp = self.head.next
            self.head.next = self.head.next.next
            if tmp.next:
                tmp.next.pre = self.head
            del self.dt[tmp.key]
            del tmp
            nd = ListNode(key, value)
            nd.next = None
            nd.pre = self.tail
            self.tail.next = nd
            self.tail = nd
            self.dt[key] = nd
        else:
            nd = ListNode(key, value)
            nd.next = None
            nd.pre = self.tail
            self.tail.next = nd
            self.tail = nd
            self.count += 1
            self.dt[key] = nd





# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

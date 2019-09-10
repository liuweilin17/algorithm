###########################################
# Let's Have Some Fun
# File Name: 232.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Mon Sep  2 10:20:10 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 232. Implement Queue using Stacks

class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.st_push = []
        self.st_pop = []


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.st_push.append(x)


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self.st_pop:
            while self.st_push:
                self.st_pop.append(self.st_push.pop())
        return self.st_pop.pop()


    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self.st_pop:
            while self.st_push:
                self.st_pop.append(self.st_push.pop())
        return self.st_pop[-1]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.st_push and not self.st_pop



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

###########################################
# Let's Have Some Fun
# File Name: 380.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Jan 27 17:56:30 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 380. Insert Delete GetRandom O(1)
# try to use space to reduce time.

import random

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.length = 0
        self.lst = []
        self.dt = {}


    def insert(self, val):
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        pos = self.dt.get(val, -1)
        if pos == -1:
            self.lst.append(val)
            self.length += 1
            self.dt[val] = self.length-1
            return True
        else:
            return False


    def remove(self, val):
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        pos = self.dt.get(val, -1)
        if pos == -1:
            return False
        else:
            tmp = self.lst[-1]
            self.lst[pos] = tmp
            self.dt[tmp] = pos
            self.dt[val] = -1
            self.lst.pop()
            self.length -= 1
            return True

    def getRandom(self):
        """
        Get a random element from the set.
        :rtype: int
        """
        if self.length < 1:
            return None
        pos = random.randint(0, self.length-1)
        return self.lst[pos]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

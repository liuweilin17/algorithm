###########################################
# Let's Have Some Fun
# File Name: 292.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Sep  4 10:22:20 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#292. Nim Game

class Solution:
    def canWinNim(self, n: int) -> bool:
        return n % 4 != 0

###########################################
# Let's Have Some Fun
# File Name: 179.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Apr 30 19:56:30 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#179. Largest Number

# customed comparator for str
class largerNum(str):
    def __lt__(x, y):
        return x+y > y+x

class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        largest_num = ''.join(sorted(map(str, nums), key=largerNum))
        # notice largest_num[0] == '0'
        return '0' if largest_num[0] == '0' else largest_num


###########################################
# Let's Have Some Fun
# File Name: lianjia2.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Sep 15 11:36:17 2018
###########################################
#coding=utf-8
#!/usr/bin/python

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

def findAll(nums, index, sumV, multi):
    count = 0
    n = len(nums)
    i = index
    while i < n:
        sumV += nums[i]
        multi *= nums[i]
        if sumV > multi:
            count += 1 + findAll(nums, i+1, sumV, multi)
        elif nums[i] == 1:
            count += findAll(nums, i+1, sumV, multi)
        else:
            break
        sumV -= nums[i]
        multi /= nums[i]
        while i<n-1 and nums[i] == nums[i+1]:
            i += 1
        i += 1
    return count

if __name__ == "__main__":
    n = int(raw_input())
    l = [int(i) for i in raw_input().split(' ', n-1)]
    l.sort()
    ret = findAll(l, 0, 0, 1) 
    print ret


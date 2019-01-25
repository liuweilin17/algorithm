###########################################
# Let's Have Some Fun
# File Name: 565.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Jan 24 17:19:58 2019
###########################################
#coding=utf-8
#!/usr/bin/python

class Solution(object):
    # my solution
    def arrayNesting1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        ret = 0
        lst = [] # memorize all the nodes in all visited sequence.
        for i in range(n):
            if not len(lst) < n: break
            j = i
            count = 0
            while True:
                if nums[j] in lst:
                    break
                else:
                    count += 1
                    lst.append(nums[j])
                    j = nums[j]
            if count > ret: ret = count
        return ret

    # In the method, it's too costly to store the nodes in a list, which involves appending and searching!
    # We simply use an array, each index stores whether the index is visited!!!!
    def arrayNesting2(self, nums):
        n = len(nums)
        visited = [False] * n
        ret = 0
        for i in range(n):
            count = 0
            j = i
            while not visited[j]:
                count += 1
                visited[j] = True
                j = nums[j]
            if count > ret: ret = count
        return ret

    # If permitted, we alter the value of nums to store if it's visited instead of an array.
    def arrayNesting3(self, nums):
        n = len(nums)
        MAX_VALUE = n
        ret = 0
        for i in range(n):
            count = 0
            j = i
            while nums[j] < n:
                count += 1
                bak = j # notice!!!!!
                j = nums[bak]
                nums[bak] = MAX_VALUE
            if ret < count: ret = count

        return ret


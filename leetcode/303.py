###########################################
# Let's Have Some Fun
# File Name: 303.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Wed Sep  4 15:43:52 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#303. Range Sum Query - Immutable

class NumArray:

    def __init__(self, nums: List[int]):
        N = len(nums)
        self.sums = [0] * (N+1)
        for i in range(1, N+1):
            self.sums[i] = self.sums[i-1] + nums[i-1]


    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j+1] - self.sums[i]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

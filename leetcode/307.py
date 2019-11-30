###########################################
# Let's Have Some Fun
# File Name: 307.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Sep  5 17:16:28 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#307. Range Sum Query - Mutable

import math

# split the array into buckets with length sqrt(n)
class NumArray1:

    def __init__(self, nums: List[int]):
        # split nums into several buckets (length is sqrt(n))
        # time: O(n)
        # space: O(sqrt(n))
        self.N = len(nums)
        if self.N == 0:
            return
        self.l = int(math.sqrt(self.N))
        length = math.ceil(self.N / self.l)
        self.sums = [0] * length
        self.nums = nums
        for i in range(self.N):
            self.sums[i//self.l] += self.nums[i]

    def update(self, i: int, val: int) -> None:
        # find the bucket and change the sums
        # time: O(1)
        if not self.N:
            return
        ind = i // self.l
        self.sums[ind] += val - self.nums[i]
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        if not self.N:
            return 0
        # get all the buckets sum
        ret = 0
        b1 = i // self.l
        b2 = j // self.l
        if b1 == b2:
            for k in range(i, j+1):
                ret += self.nums[k]
        else:
            for k in range(i, (b1+1)*self.l):
                ret += self.nums[k]
            for k in range(b1+1, b2):
                ret += self.sums[k]
            for k in range(b2*self.l, j+1):
                ret += self.nums[k]

        return ret

# segment tree
class NumArray1:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.N = len(self.nums)
        if not self.N: return

        # build segment tree
        # say nd is the sum of [i, j]
        # then
        # nd.left is the sum of [i, (i+j)//2]
        # nd.right is the sum of [(i+j)//2+1, j]
        # time: O(N)
        self.seg_tree = [0] * 2 * self.N
        for i in range(self.N, 2*self.N):
            self.seg_tree[i] = self.nums[i-self.N]
        for i in range(self.N-1, -1, -1):
            self.seg_tree[i] = self.seg_tree[2*i] + self.seg_tree[2*i+1]

    def update(self, i: int, val: int) -> None:
        if not self.N: return
        # time : O(logN)
        ind = i + self.N
        while ind > 0:
            self.seg_tree[ind] += val - self.nums[i]
            ind //= 2
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        # Notice the way to calculate the sum in segment tree
        if not self.N: return
        ret = 0
        i += self.N
        j += self.N
        while i <= j:
            if i % 2 == 1:
                ret += self.seg_tree[i]
                i += 1
            if j % 2 == 0:
                ret += self.seg_tree[j]
                j -= 1
            i //= 2
            j //= 2

        return ret

class TreeNode:
    def __init__(self, begin, end, sumV):
        self.begin = begin
        self.end = end
        self.sumV = sumV
        self.left = None
        self.right = None

def buildTree(nums, begin, end):
    if begin > end:
        return None
    elif begin == end:
        return TreeNode(begin, end, nums[begin])
    else:
        ret = TreeNode(begin, end, 0)
        mid = (begin + end) // 2
        ret.left = buildTree(nums, begin, mid)
        ret.right = buildTree(nums, mid+1, end)
        if ret.left: ret.sumV += ret.left.sumV
        if ret.right: ret.sumV += ret.right.sumV
        return ret

# Use node to implement Segment Tree
class NumArray3:

    def __init__(self, nums: List[int]):
        N = len(nums)
        self.root = buildTree(nums, 0, N-1)

    def update(self, i: int, val: int) -> None:
        self.updateSub(self.root, i, val)

    def updateSub(self, nd, i, val):
        # We could ensure index i is in the children of nd
        if nd.begin == nd.end: nd.sumV = val
        else:
            mid = (nd.begin + nd.end) // 2
            if i <= mid:
                self.updateSub(nd.left, i, val)
            else:
                self.updateSub(nd.right, i, val)
            nd.sumV = nd.left.sumV + nd.right.sumV

    def sumRange(self, i: int, j: int) -> int:
        return self.sumRangeSub(self.root, i, j)

    def sumRangeSub(self, nd, i, j):
        if not nd: return 0
        elif nd.begin == i and j == nd.end:
            return nd.sumV
        else:
            mid = (nd.begin + nd.end) // 2
            if mid < i:
                return self.sumRangeSub(nd.right, i, j)
            elif mid >= j:
                return self.sumRangeSub(nd.left, i, j)
            else:
                return self.sumRangeSub(nd.left, i, mid) + self.sumRangeSub(nd.right, mid+1, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

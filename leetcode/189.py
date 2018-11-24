###########################################
# Let's Have Some Fun
# File Name: 189.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Fri Nov 23 21:04:02 2018
###########################################
#coding=utf-8
#!/usr/bin/python
# 189. Rotate Array

class Solution:
    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        l = len(nums)
        ret = [0] * l
        for i in range(l):
            ret[(i + k)%l] = nums[i]
        for i in range(l):
            nums[i] = ret[i]

    # 从0开始替换：k，k+k, k+k+k ...
    # 如果回到0，从1开始替换：1，1+k, 1+k+k ...
    # 如果全部都被替换，退出
    def rotate2(self, nums, k):
        if k == 0:
            return
        l = len(nums)
        c = 0 # 被替换元素的个数
        begin = 0 # 开始进行替换位置
        cur = 0 # 遍历指针
        t = nums[cur] # t存储已经被替换的元素
        while True:
            nt = (cur+k) % l
            # 替换回到开始位置，则从begin+1开始
            if nt == begin:
                nums[nt] = t
                c += 1
                if c >= l:
                    return
                begin = nt + 1
                cur = begin
                t = nums[cur]
            # t 替换 nt位置元素，同时 使用t保留nt位置元素
            else:
                tmp = nums[nt]
                nums[nt] = t
                t = tmp
                cur = nt
                c += 1
                if c >= l:
                    return
            #print(nums)

if __name__ == '__main__':
    s = Solution()

    a, k = [1,2,3,4,5,6,7],3
    s.rotate2(a,k)
    print(a)
    a, k = [-1,-100,3,99],2
    s.rotate2(a,k)
    print(a)
    a, k = [1,2],1
    s.rotate2(a, k)
    print(a)
    a, k = [1, 2], 2
    s.rotate2(a, k)
    print(a)
    a, k = [1,2,3,4,5,6],2
    s.rotate2(a, k)
    print(a)


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
    
    # in place, using cyclic replacement
    def rotate3(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k = k % n
        if k == 0: return

        count = 0
        for i in range(n):
            start = i
            cur = start
            preV = nums[cur]
            flag = 1
            while cur != start or flag:
                nxt = (cur + k) % n
                bak = nums[nxt]
                nums[nxt] = preV
                cur = nxt
                preV = bak
                flag = 0
                count += 1
            if count == n:
                break

    # use some tricks
    def rotate4(self, nums, k):
        l = len(nums)
        if l == 0: return
        k = k % l
        if k == 0: return

        nums.reverse()
        # reverse the first k elements
        for i in range((k - 2) // 2 + 1):
            tmp = nums[i]
            nums[i] = nums[k - i - 1]
            nums[k - i - 1] = tmp

        # reverse the rest n-k elements
        for i in range(k, (l - k - 2) // 2 + k + 1):
            tmp = nums[i]
            nums[i] = nums[l + k - 1 - i]
            nums[l + k - 1 - i] = tmp

if __name__ == '__main__':
    s = Solution()
    #print(s.rotate([1,2,3,4,5,6,7,8,9], 3))
    nums=[1,2,3,4,5,6]
    print(nums)
    s.rotate2(nums, 4)
    print(nums)


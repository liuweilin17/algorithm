###########################################
# Let's Have Some Fun
# File Name: 46.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Jan  1 12:31:49 2019
###########################################
#coding=utf-8
#!/usr/bin/python
import itertools

class Solution:
    def permute1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        return list(itertools.permutations(nums, len(nums)))

    def permute2(self, nums):
        ret = [[]]
        for n in nums:
            new_ret = []
            for i in range(len(ret)):
                tmp = ret[i]
                tmp.append(n)
                for j in range(len(tmp)):
                    tmp[j], tmp[-1] = tmp[-1], tmp[j]
                    new_ret.append(tmp[:]) # notice!!! new_ret.append(tmp) is wrong!!!
                    tmp[j], tmp[-1] = tmp[-1], tmp[j]
            ret = new_ret
        return ret

    # backtracking
    # link:
    # https://leetcode.com/problems/permutations/discuss/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning)
    def permute3(self, nums):
        ret = []
        self.backtrack(ret, [], nums)
        return ret

    def backtrack(self, ret, tmp, nums):
        if len(tmp) == len(nums):
            ret.append(tmp[:])
        else:
            for n in nums:
                if n not in tmp:
                    tmp.append(n)
                    self.backtrack(ret, tmp[:], nums)
                    tmp.pop()


if __name__ == '__main__':
    s = Solution()
    print(s.permute1([1,2,3]))
    print(s.permute2([1,2,3]))
    print(s.permute3([1,2,3]))

###########################################
# Let's Have Some Fun
# File Name: 377.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sat Feb  9 16:56:42 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#377. Combination Sum IV

# when backtrack is of great cost, take dp into consideration
# The reason why dp is more efficient is that d memorizes the combinations of given sum,
# while recursive method may calculate the combinations of given sum mulitple times.
# For example, after [1,1] and [2], we have to calculte combinations of target-2 twice.
class Solution:
    def combinationSum4(self, nums: 'List[int]', target: 'int') -> 'int':
        # d[i], the number of combinations with sum of i
        d = [0] * (target+1)
        d[0] = 1
        for i in range(1, target+1):
            for num in nums:
                if num <= i:
                    d[i] += d[i-num]

        return d[target]





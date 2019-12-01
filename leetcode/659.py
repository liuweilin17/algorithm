###########################################
# Let's Have Some Fun
# File Name: 659.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Sun Dec  1 11:23:51 2019
###########################################
#coding=utf-8
#!/usr/bin/python
class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        count = collections.Counter(nums)
        target = collections.defaultdict(int)
        for num in nums:
            if count[num] == 0: # the number has been assigned to a subsequence
                continue
            elif target[num] > 0: # before num, there exists some subsequence
                target[num] -= 1 # delete 
                target[num+1] += 1 # add num and has a new subsequence
                count[num] -= 1 # num has been added
            elif count[num+1] >0 and count[num+2]>0:
                count[num] -= 1 # num has been added
                count[num+1] -= 1
                count[num+2] -= 1
                target[num+3] += 1
            else:
                return False
        return True
                
        

###########################################
# Let's Have Some Fun
# File Name: 464.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Mar  5 16:54:09 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#464. Can I Win

class Solution:
    # brutal method, simulating the game process
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # if the sum of [1, maxChoosableInteger] is smaller than desiredTotal,
        # then both player cannot win the game. return False.
        if (1+maxChoosableInteger) * maxChoosableInteger // 2 < desiredTotal:
            return False
        
        memo = {}
        def helper(nums, desiredTotal):
            hash = str(nums)
            if hash in memo: return memo[hash]
            # if the biggest number is bigger or equal to desiredTotal, then choose it and win.
            if nums[-1] >= desiredTotal: return True
            
            for i in range(len(nums)):
                # force the second player to loose.
                if not helper(nums[:i]+nums[i+1:], desiredTotal-nums[i]):
                    memo[hash] = True
                    return True
            memo[hash] = False
            return False
        
        return helper(list(range(1, maxChoosableInteger+1)), desiredTotal)
        

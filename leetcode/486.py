###########################################
# Let's Have Some Fun
# File Name: 486.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Tue Mar  5 09:25:32 2019
###########################################
#coding=utf-8
#!/usr/bin/python

#486. Predict the Winner

class Solution:
    # recursion O(2^n)
    def PredictTheWinner1(self, nums: List[int]) -> bool:
        N = len(nums)

        def helper(begin, end, turn):
            if begin == end:
                return turn * nums[begin]
            if turn == 1: # total_sum += nums[begin] or nums[end]
                return max(nums[begin] + helper(begin+1, end, -1), nums[end] + helper(begin, end-1, -1))
            if turn == -1: # total_sum += -nums[begin] or -nums[end]
                return min(-nums[begin] + helper(begin+1, end, 1), -nums[end] + helper(begin, end-1, 1))

        # if total_sum >= 0, then player1 wins
        return helper(0, N-1, 1) >= 0

        return helper(0, N-1, 1, 0, 0)

   # recursion with space, O(n^2)
   def PredictTheWinner2(self, nums: List[int]) -> bool:
        N = len(nums)
        memo = []
        for i in range(N):
            memo.append([None] * N)

        def helper(begin, end):
            if memo[begin][end]: return memo[begin][end]
            if begin == end:
                return nums[begin]
            # whether it's player1 or player2, always minus the sum of the other player.
            a = nums[begin] - helper(begin+1, end)
            b = nums[end] - helper(begin, end-1)
            memo[begin][end] = max(a, b)
            return max(a, b)
        # since play1 is the first to pick given nums[0:N],
        # memo[0][N-1] = max(nums[0]-memo[1][N-1], nums[N-1]-memo[0][N-2])
        # make the sum score of player2 < 0 and the sum score of player1 > 0
        # when memo[0][N-1] or helper(0, N-1) >= 0 indicates that player1 wins.
        return helper(0, N-1) >= 0
    
    # similar to approach 2, we use dp[i][j] to memorize max-value of nums[i:j]
    # result is dp[0][N-1]
    # dp[i][j] = max(nums[i] - dp[i+1][j], nums[j]-dp[i][j-1])
    def PredictTheWinner3(self, nums: List[int]) -> bool:
        N = len(nums)
        dp = []
        for i in range(N):
            dp.append([0] * N)

        for end in range(1, N):
            for begin in range(end-1, -1, -1):
                a = nums[begin] - dp[begin+1][end]
                b = nums[end] - dp[begin][end-1]
                dp[begin][end] = max(a, b)

        # since player1 is the first to pick given nums[0:N],
        # dp[0][N-1] = max(nums[0]-dp[1][N-1], nums[N-1]-dp[0][N-2])
        # make the sum score of player2 < 0 and the sum score of player1 > 0
        # when dp[0][N-1]>=0 indicates that player1 wins.
        return dp[0][N-1] >= 0

    # similar to approach 3, we use 1-d dp, begin is redundant
    # since we can override the results of previous rows.
    # NOTICE: the order of begin and end should be switched !!! 
    def PredictTheWinner4(self, nums: List[int]) -> bool:
        N = len(nums)
        dp=[0] * N

        # for end in range(1, N):
        #     for begin in range(end-1, -1, -1):
        #         a = nums[begin] - dp[end]
        #         b = nums[end] - dp[end-1]
        #         dp[end] = max(a, b)
        for begin in range(N-1, -1, -1):
            for end in range(begin+1, N):
                a = nums[begin] - dp[end]
                b = nums[end] - dp[end-1]
                dp[end] = max(a, b)

        return dp[N-1] >= 0

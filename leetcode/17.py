###########################################
# Let's Have Some Fun
# File Name: 17.py
# Author: Weilin Liu
# Mail: liuweilin17@qq.com
# Created Time: Thu Jan 10 20:37:32 2019
###########################################
#coding=utf-8
#!/usr/bin/python

# 17. Letter Combinations of a Phone Number

class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        dt = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        ret = []
        self.backtrack(digits, dt, [], 0, ret)
        return ret

    def backtrack(self, digits, dt, tmp, i, ret):
        if len(tmp) == len(digits):
            if len(tmp) > 0:
                ret.append(''.join(tmp))
            return
        for c in dt[digits[i]]:
            tmp.append(c)
            self.backtrack(digits, dt, tmp, i+1, ret)
            tmp.pop()



if __name__ == '__main__':
    s = Solution()
    print(s.letterCombinations("23"))
    print(s.letterCombinations(""))


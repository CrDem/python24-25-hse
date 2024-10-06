"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-valid-parentheses/description
"""


class Solution:
    def __init__(self):
        self.res = 0

    def resFinding(self, s, r: str):
        leftPointer = 0
        currP = 0
        for charId in range(len(s)):
            if s[charId] == r:
                currP += 1
            else:
                if currP > 0:
                    currP -= 1
                else:
                    leftPointer = charId + 1
            if (currP == 0): self.res = max(self.res, charId - leftPointer + 1)

    def longestValidParentheses(self, s: str) -> int:
        self.resFinding(s, '(')
        self.resFinding(s[::-1], ')')
        return self.res

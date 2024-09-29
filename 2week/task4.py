"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/count-and-say/description/
"""


class Solution:
    def RLE(self, s: str) -> str:
        counter = 1
        res = ""
        for sId in range(len(s)):
            if sId == len(s) - 1 or s[sId] != s[sId + 1]:
                res += str(counter) + s[sId]
                counter = 1
            else:
                counter += 1
        return res

    def countAndSay(self, n: int) -> str:
        if n == 1:
            return '1'
        else:
            return self.RLE(self.countAndSay(n - 1))

"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/zigzag-conversion/description/
"""
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or len(s) == 1:
            return s
        upSkip = 0
        downSkip = numRows*2 - 2
        res = ''
        for start in range (numRows):
            gravity = True
            curr = start
            while curr < len(s):
                if gravity:
                    if downSkip > 0:  res += s[curr]
                    curr += downSkip
                    gravity = False
                else:
                    if upSkip > 0:  res += s[curr]
                    curr += upSkip
                    gravity = True
            upSkip += 2
            downSkip -= 2
        return res

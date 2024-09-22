"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/string-to-integer-atoi/description/
"""
class Solution:
    def myAtoi(self, s: str) -> int:
        sign = 1
        signMet = False
        number = False
        trueNumber = False
        res = 0
        for char in s:
            if char > '9': break
            if not number:
                if char > '0':
                    number = True
                    trueNumber = True
                    res += int(char)
                    continue
                if char == '0': 
                    number = True
                    continue
                if char == ' ' and not signMet: continue
                if (char == '-' or char == '+') and not signMet:
                    signMet = True
                    if char == '-': sign = -1
                    continue
                break
            else:
                if char < '0': break
                if char == '0' and not trueNumber: continue
                trueNumber = True
                res *= 10
                res += int(char)
        if res*sign < -2147483648: return -2147483648
        if res*sign > 2147483647: return 2147483647
        return res*sign

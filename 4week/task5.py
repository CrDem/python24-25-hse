"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/multiply-strings/description
"""


class Solution:
    def multiply(self, num1: str, num2: str):
        if num1 == "0" or num2 == "0":
            return "0"

        res = [0] * (len(num1) + len(num2))

        for rId in range(len(num1) - 1, 0 - 1, -1):
            for fId in range(len(num2) - 1, 0 - 1, -1):
                res[rId + fId + 1] += int(num1[rId]) * int(num2[fId])
                val = res[rId + fId + 1]
                if val >= 10:
                    res[rId + fId] += val // 10
                    res[rId + fId + 1] = val % 10

        while res[0] == 0:
            res.pop(0)
        return "".join(map(str, res))

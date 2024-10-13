"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/generate-parentheses/description
"""


class Solution:
    def __init__(self):
        self.res = []

    def wayGenerator(self, g, v, n: int, way: str):
        if (g == n and v == n):
            self.res.append(way)
            return
        if (g > n or v > g): return
        self.wayGenerator(g, v + 1, n, way + ')')
        self.wayGenerator(g + 1, v, n, way + '(')

    def generateParenthesis(self, n: int) -> List[str]:
        self.wayGenerator(1, 0, n, "(")
        return self.res

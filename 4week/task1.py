"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/letter-combinations-of-a-phone-number/description
"""
from itertools import product


class Solution:
    def letterCombinations(self, digits: str) -> list[str]:
        res = []
        res1 = []
        dictionary = [['a', 'b', 'c'], ['d', 'e', 'f'], ['g', 'h', 'i'], ['j', 'k', 'l'], ['m', 'n', 'o'],
                      ['p', 'q', 'r', 's'], ['t', 'u', 'v'], ['w', 'x', 'y', 'z']]
        for number in digits:
            res.append(dictionary[int(number) - 2])
        if len(digits) > 0:
            return ["".join(l) for l in product(*res)]
        else:
            return res1
"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        lastMeet = [-1] * 256
        start = 0
        res = 0
        for curr in range(len(s)):
            start = max(start, lastMeet[ord(s[curr])] + 1)
            lastMeet[ord(s[curr])] = curr
            res = max(res, curr-start+1)
        return res
        

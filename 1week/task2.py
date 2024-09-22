"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/description/
"""
class Solution:
    def longestPalindrome(self, s: str) -> str:
        resL = 1
        resS = s[0]
        for space in range(len(s)):
            if resL > (len(s) - space):
                return resS
            for i in range(2):
                if i == 0:
                    side = 1
                else:
                    side = -1
                doubledCenterID = len(s) + space*side
                centerID = doubledCenterID/2

                start = int(centerID - ( 2 - (doubledCenterID % 2) ) /2  )
                finish = int(centerID + ( 2 - (doubledCenterID % 2) ) /2)
                while ( (start >= 0) and (finish <= len(s)-1) ):
                    if (s[start] != s[finish]):
                        break
                    start -= 1
                    finish += 1
                if (resL < (finish-start-1)):
                    resS = s[start+1:finish-1] + s[finish-1]
                    resL = finish-start-1
        return resS

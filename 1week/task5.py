"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/integer-to-roman/description/
"""
class Solution:
    def intToRoman(self, num: int) -> str:
        res = ''
        while num > 0:
            while num >= 1000:
                num -= 1000
                res += 'M'
                continue
            if str(num)[0] == '9':
                if num >= 900:
                    num -= 900
                    res += "CM"
                    continue
                if num >= 90:
                    num -= 90
                    res += "XC"
                    continue
                if num >= 9:
                    num -= 9
                    res += "IX"
                    continue
            if str(num)[0] == '4':
                if num >= 400:
                    num -= 400
                    res += "CD"
                    continue
                if num >= 40:
                    num -= 40
                    res += "XL"
                    continue
                if num >= 4:
                    num -= 4
                    res += "IV"
                    continue
            if num >= 500:
                num -= 500
                res += 'D'
                continue
            if num >= 100:
                num -= 100
                res += 'C'
                continue
            if num >= 50:
                num -= 50
                res += 'L'
                continue
            if num >= 10:
                num -= 10
                res += 'X'
                continue
            if num >= 5:
                num -= 5
                res += 'V'
                continue
            if num >= 1:
                num -= 1
                res += 'I'
                continue
        return res        
# ne beite ya prosto toropilsya + ne bilo sil dumatb

class Solution(object):
    def romanToInt(self, s):
        roman_num = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        } 
        num = 0
        for i in range(len(s)):
            if i < len(s) - 1 and roman_num[s[i]] < roman_num[s[i + 1]]:
                num -= roman_num[s[i]]
            else:
                num += roman_num[s[i]]
        return num

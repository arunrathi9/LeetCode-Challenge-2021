"""
Given a roman numeral, convert it to an integer.

Input: s = "IV"
Output: 4

"""


class Solution:
    def romanToInt(self, s):
        mapping = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        prev = mapping['M']
        for char in s:
            # get decimal value of character
            current_num = mapping[char]
            # add it to result
            result += current_num
            if prev < current_num:
                result -= prev*2
            # update prev
            prev = current_num

        return result

    def romanToInt2(self, s):
        mapping = {'I': 1, 'V': 5, 'X': 10,
                   'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        no = 0
        temp = ""
        for i in range(len(s)):
            temp_no = mapping[s[-i-1]]
            if no > 0:
                if mapping[temp] > temp_no:
                    no -= temp_no
                else:
                    no += temp_no
            else:
                no += temp_no
            temp = s[-i-1]

        return no


sol = Solution()
print(sol.romanToInt('II'))
print(sol.romanToInt('IV'))
print(sol.romanToInt('IX'))
print(sol.romanToInt('LVIII'))
print(sol.romanToInt('MCMXCIV'))

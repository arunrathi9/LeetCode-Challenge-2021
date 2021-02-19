"""
Minimum Remove to Make Valid Parentheses

Given a string s of '(' , ')' and lowercase English characters. Your task is to remove
the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting
parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:
    It is the empty string, contains only lowercase characters, or
    It can be written as AB (A concatenated with B), where A and B are valid strings, or
    It can be written as (A), where A is a valid string.

Input: s = "(a(b(c)d)"
Output: "a(b(c)d)
"""


class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = list(s)
        left_parr = 0
        left_ind = []
        for i in range(len(s)):
            if s[i] == ')' and left_parr == 0:
                s[i] = ''
            elif s[i] == '(':
                left_parr += 1
                left_ind.append(i)
            elif s[i] == ')' and left_parr > 0:
                left_parr -= 1
                left_ind.pop()

        if len(left_ind) > 0:
            for j in left_ind:
                s[j] = ''

        return ''.join(s)


sol = Solution()
print(sol.minRemoveToMakeValid('()())()'))

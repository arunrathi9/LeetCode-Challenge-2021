"""
Given two strings s and t , write a function to determine if t is an anagram of s.

Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false

"""


class Solution:
    def isAnagram(self, s: str, t: str):

        # method1:
        if len(s) != len(t):
            return False
        else:
            return {k: s.count(k) for k in set(s)} == {k: t.count(k) for k in set(t)}

        # method2:
        if len(s) != len(t):
            return False

        def counter(s):
            d = dict()
            for i in s:
                if i not in d.keys():
                    d[i] = 1
                else:
                    d[i] += 1

            return d

        if counter(s) == counter(t):
            return True
        else:
            return False


sol = Solution()
print(sol.isAnagram('abc', 'cab'))
print(sol.isAnagram('abc', 'bcd'))

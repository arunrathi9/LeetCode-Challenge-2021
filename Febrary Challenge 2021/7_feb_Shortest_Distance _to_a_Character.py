"""
Problem: Given a string s and a character c that occurs in s, return an array of integers answer
         where answer.length == s.length and answer[i] is the shortest distance from s[i] to the character c in s.


Example 1:
Input: s = "loveleetcode", c = "e"
Output: [3,2,1,0,1,0,0,1,2,2,1,0]

Example 2:
Input: s = "aaab", c = "b"
Output: [3,2,1,0]

"""

import math


class Solution:

    def shortesttochar(self, s: str, c: str):
        """
        implemented by me 
        Noted: Time Complexity = 32ms O(n)
                Space Complexity = O(n)
        """

        dist = []
        c_ind = []
        for i in range(len(s)):
            if s[i] == c:
                c_ind.append(i)

        c_count = 0
        for i in range(len(s)):
            if s[i] == c:
                dist.append(0)
                if c_count < len(c_ind)-1:
                    c_count += 1
            elif c_count == 0:
                dist.append(abs(c_ind[c_count]-i))
            elif abs(c_ind[c_count-1]-i) <= abs(c_ind[c_count]-i):
                dist.append(abs(c_ind[c_count-1]-i))
            else:
                dist.append(abs(c_ind[c_count]-i))

        return dist

    def fun3(self, s, c):
        """
        taken from leetcode 
        Noted: Time = 76ms
        """
        dist = [len(s)] * len(s)
        c_ind = []
        for i in range(len(s)):
            if s[i] == c:
                c_ind.append(i)
                dist[i] = 0

        c_count = 0
        for i in range(len(s)):
            if s[i] == c:
                if c_count < len(c_ind)-1:
                    c_count += 1
            elif c_count == 0:
                dist[i] = abs(c_ind[c_count]-i)
            elif abs(c_ind[c_count-1]-i) <= abs(c_ind[c_count]-i):
                dist[i] = abs(c_ind[c_count-1]-i)
            else:
                dist[i] = abs(c_ind[c_count]-i)
        return dist

    def fun4(self, S, C):
        """
        taken from leetcode
        Noted: run time = 20ms
        """
        ans = [None] * len(S)

        prev = -math.inf
        for i, char in enumerate(S):
            if char == C:
                prev = i
                ans[i] = 0
            else:
                ans[i] = i - prev

        prev = math.inf
        for i in reversed(range(len(S))):
            char = S[i]
            if char == C:
                prev = i
                ans[i] = 0
            else:
                ans[i] = min(ans[i], prev - i)

        return ans


check = Solution()
print(check.shortesttochar('loveleetcode', 'e'))

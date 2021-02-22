"""
Longest Word in Dictionary through Deleting
Given a string and a string dictionary, find the longest string in the dictionary that can
be formed by deleting some characters of the given string. If there are more than one
possible results, return the longest word with the smallest lexicographical order.
If there is no possible result, return the empty string.

Example: Input: s = "abpcplea", d = ["ale","apple","monkey","plea"]
output: apple
"""


class Solution:
    def findLongestWord(self, s, d):

        d.sort()
        d.sort(reverse=True, key=len)
        for i in range(len(d)):
            curr = 0
            for j in range(len(s)):
                if s[j] == d[i][curr]:
                    curr += 1
                    if curr == len(d[i]):
                        return d[i]
        return ""

    def findLongestWord2(self, s, d):
        d.sort(key=lambda x: (-len(x), x))

        for word in d:

            last = 0
            for char in word:
                last = s.find(char, last)+1
                if last == 0:
                    break
            else:
                return word
        return ""


sol = Solution()
print(sol.findLongestWord2("abpcplea", ["ale", "apple", "monkey", "plea"]))
print(sol.findLongestWord2("abpcplea", ['b', "a", "c"]))
print(sol.findLongestWord2("apple", ["zxc", "vbn"]))

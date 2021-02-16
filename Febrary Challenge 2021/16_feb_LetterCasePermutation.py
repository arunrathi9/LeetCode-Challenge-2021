"""
Letter Case Permutation

Problem statement: Given a string S, we can transform every letter individually to be lowercase
or uppercase, to create another string. Return a list of all possible strings we could create.
You can return the output in any order.

Example 1:
Input: S = "a1b2"
Output: ["a1b2","a1B2","A1b2","A1B2"]

"""


class Solution:
    def letterCasePermutation(self, S: str):
        """
        :type S: str
        :rtype: List[str]
        """
        ans_list = [[]]
        for c in S:
            if c.isalpha():
                for i in range(len(ans_list)):
                    ans_list.append(ans_list[i][:])
                    ans_list[i].append(c.lower())
                    ans_list[-1].append(c.upper())
            else:
                for l in ans_list:
                    l.append(c)

        return list(map(''.join, ans_list))

    # method taken from leetcode
    def letterCasePermutation2(self, S: str):
        def bt(res, currstr, orig_str, idx):

            if len(currstr) == len(orig_str):
                res.append(currstr)
                return

            if orig_str[idx].isalpha():
                bt(res, currstr + orig_str[idx].lower(), orig_str, idx + 1)
                bt(res, currstr + orig_str[idx].upper(), orig_str, idx + 1)
            else:
                bt(res, currstr + orig_str[idx], orig_str, idx+1)

        res = []
        currstr = ""
        orig_str = S

        bt(res, currstr, orig_str, 0)
        return res


sol = Solution()
res = sol.letterCasePermutation2('a1b2c3d4')
print(res)
print(len(res))

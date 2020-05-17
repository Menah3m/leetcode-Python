
'''
leetcode-05
给定一个字符串 s，找到 s 中最长的回文子串。你可以假设 s 的最大长度为 1000。

'''





class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            start = max(0, i-len(res)-1)
            temp = s[start:i+1]
            if temp == temp[::-1]:
                res = temp
            else:
                temp = temp[1:]
                if temp == temp[::-1]:
                    res = temp
        return res
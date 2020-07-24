"""
编写一个函数，以字符串作为输入，反转该字符串中的元音字母。

示例 1:

输入: "hello"
输出: "holle"
示例 2:

输入: "leetcode"
输出: "leotcede"

来源：LeetCode-345
链接：https://leetcode-cn.com/problems/reverse-vowels-of-a-string
"""

class Solution:
    def reverseVowels(self, s: str) -> str:
        l, r = 0, len(s)-1
        s = list(s)
        cache = ['a','e','i','o','u','A','E','I','O','U']
        while l < r:
            if s[l] not in cache:
                l += 1
                continue
            if s[r] not in cache:
                r -= 1
                continue
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        return ''.join(s)
        
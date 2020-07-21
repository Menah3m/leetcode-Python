"""
给定一个字符串，验证它是否是回文串，只考虑字母和数字字符，可以忽略字母的大小写。

说明：本题中，我们将空字符串定义为有效的回文串。

示例 1:

输入: "A man, a plan, a canal: Panama"
输出: true
示例 2:

输入: "race a car"
输出: false

来源：LeetCode-125
链接：https://leetcode-cn.com/problems/valid-palindrome

"""

# 双指针  关键点：如何去掉除数字和字母外的其他字符
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 0: return True
        s = ''.join(c for c in s if c not in string.punctuation)
        s = ''.join(s.split())
        s= s.lower()
        start, end = 0, len(s)-1
        while start < end:
            if s[start] != s[end]:
                return False
            start += 1
            end -= 1
        return True

class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = s.replace(' ','')
        cache = ''
        for i in s:
            if not i.isdigit() and not i.isalpha():
                continue
            else:
                cache += i
        if not cache:
            return True
        l, r = 0, len(cache)-1
        while l <= r:
            if cache[l] != cache[r]:
                return False
            else:
                l += 1
                r -= 1
        return True
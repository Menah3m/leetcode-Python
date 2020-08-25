"""
给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

 

示例：

s = "leetcode"
返回 0

s = "loveleetcode"
返回 2

来源：LeetCode-387
链接：https://leetcode-cn.com/problems/first-unique-character-in-a-string

"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        dic = {}
        for c in s:
            dic[c] = c not in dic
        for i in range(len(s)):
            if dic[s[i]]:
                return i
        return -1
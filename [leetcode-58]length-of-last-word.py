"""
给定一个仅包含大小写字母和空格 ' ' 的字符串 s，返回其最后一个单词的长度。如果字符串从左向右滚动显示，那么最后一个单词就是最后出现的单词。

如果不存在最后一个单词，请返回 0 。

说明：一个单词是指仅由字母组成、不包含任何空格字符的 最大子字符串。

 

示例:

输入: "Hello World"
输出: 5

来源：LeetCode-58
链接：https://leetcode-cn.com/problems/length-of-last-word

"""
# 思路1
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        if not s:
            return 0
        s = s.rstrip()
        count = 0
        for i in s[::-1]:
            if i == " ":
                return count
            else:
                count += 1
        return count

# 思路2
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.rstrip()
        if not s:
            return 0
        return len(s.split()[-1])
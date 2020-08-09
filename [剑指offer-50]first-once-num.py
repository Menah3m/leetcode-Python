"""
在字符串 s 中找出第一个只出现一次的字符。如果没有，返回一个单空格。 s 只包含小写字母。

示例:

s = "abaccdeff"
返回 "b"

s = "" 
返回 " "
 

来源：剑指offer-50
链接：https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof

"""

# 思路： 哈希表，第一次遍历到时设置value为 True，后面再次遍历到的时候设置value为False
# 再次遍历s，判断dic中的键值，返回第一个值为True的键（说明只遍历到一次）
class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for i in s:
            dic[i] = not i in dic
        for i in s:
            if dic[i]:
                return i
        return " "


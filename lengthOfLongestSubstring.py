'''

'''

'''
leetcode 3
无重复字符的最长子串
思路： 1.从头开始遍历字符串，将每个字符存入字典中
      2.每次遍历得到的字符同字典进行比较，如果不存在字典中，则更新 长度
      如果已经存在，则计算长度时的start从字典中该字符的下一位算起
      
    

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0 or len(s)==1:   #边界判断
            return len(s)
        start = 0                      # 子串长度计算的start
        res = {}                       # 存放遍历过的未重复的字符
        length = 0                     # 初始长度
        for i in range(len(s)):
            if s[i] in res and start <= res[s[i]]:
                start = res[s[i]] + 1
            length = max(length, i - start + 1)
            res[s[i]] = i
        return length



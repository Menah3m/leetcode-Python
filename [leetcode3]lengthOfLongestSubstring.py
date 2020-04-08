'''

'''

'''
leetcode 3
无重复字符的最长子串
思路1： 1.从头开始遍历字符串，将每个字符存入字典中
      2.每次遍历得到的字符同字典进行比较，如果不存在字典中，则更新 长度
      如果已经存在，则计算长度时的start从字典中该字符的下一位算起
      
    

'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:   #边界判断
            return 0
        start = 0                      # 子串长度计算的start
        res = {}                       # 存放遍历过的未重复的字符
        length = 0                     # 初始长度
        for i in range(len(s)):
            if s[i] in res and start <= res[s[i]]:
                start = res[s[i]] + 1
            length = max(length, i - start + 1)
            res[s[i]] = i
        return length

'''
思路2：
滑动窗口，用滑动窗口的长度来表示最大子串的长度，
遍历字符串，如果遍历到的字符不重复，则添加到字典中，
如果重复，则删除掉滑动窗口中的一个字符。
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0

        res = set()                          #定义一个存放字符的字典（此处用集合）
        start = 0                            #存放字典的头指针
        cur_len = 0
        maxLen = 0

        for i in range(len(s)):              #读取字符串的字符，每次读取都把当前字符串长度加1
            cur_len += 1
            while s[i] in res:               #判断读取到的字符是否存在于 保存的字典中，如果存在，则删除字典中最前头的字符
                res.remove(s[start])         #并且把当前长度减1，start指针往后移动1
                cur_len -= 1
                start += 1
            res.add(s[i])                    #如果不存在已保存的字典中，则添加到字典中
            maxLen = max(maxLen, cur_len)    #返回长度
        return maxLen



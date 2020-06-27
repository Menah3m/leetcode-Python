"""
编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

示例 1:

输入: ["flower","flow","flight"]
输出: "fl"
示例 2:

输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。

来源：LeetCode-14
链接：https://leetcode-cn.com/problems/longest-common-prefix

"""




class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       
        if len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        
        minlen = min([len(x) for x in strs])     //确定数组中最短的字符串长度
        
        end = 0                                  // 定义字符串下标
        while end < minlen:                      
            for i in range(1,len(strs)):         
                if strs[i][end] != strs[i-1][end]: 
                    return strs[0][:end]
            end += 1
        return strs[0][:end]

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

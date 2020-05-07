


'''
投机取巧法
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" or haystack == needle: return 0
        if len(haystack) < len(needle):
            return -1
        
        return haystack.find(needle) if needle in haystack else -1

'''
暴力法
'''
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" or haystack == needle: return 0
        if len(haystack) < len(needle): return -1

        m = len(needle)
        for i in range(len(haystack)-m+1):
            if haystack[i:i+m] == needle:
                return i
        return -1
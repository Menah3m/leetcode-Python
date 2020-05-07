class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "" or haystack == needle: return 0
        if len(haystack) < len(needle):
            return -1
        
        return haystack.find(needle) if needle in haystack else -1
        
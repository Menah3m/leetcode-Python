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
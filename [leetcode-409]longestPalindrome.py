class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0
        r = collections.Counter(s)
        odd_flag = 0
        for i in r:
            if r[i]%2 == 0:
                res += r[i]
            else:
                odd_flag = 1
                res += r[i] - 1
        return res + 1 if odd_flag == 1 else res
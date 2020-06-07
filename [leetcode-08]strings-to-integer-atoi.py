


class Solution:
    def myAtoi(self, str: str) -> int:
        str = str.lstrip()
        if len(str)==0 or (str[0].isdigit()==False and str[0] not in ["-", "+"]):
            return 0
        res, i = str[0], 1
        while i < len(str) and str[i].isdigit():
            res += str[i]
            i += 1
        try:
            res = int(res)
            return min(max(res, -2**31), 2**31-1)
        except:
            return 0
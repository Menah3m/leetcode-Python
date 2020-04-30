class Solution:
    def printNumbers(self, n: int) -> List[int]:
        num = pow(10, n)
        re = []
        for i in range(1,num):
            re.append(i)
        return re

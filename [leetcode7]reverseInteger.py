

'''

'''


'''
leetcode.7
整数反转
思路：
    1.判断正负：
        正：先转字符串，再转列表，然后反转列表后转字符串，再转整数
        负：先把整数转换成正数，然后执行正数情况下的步骤，最后结果取负即可
        0：返回0
    2.判断结果边界
'''

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            res = int(''.join(list(str(x))[::-1]))
        if x < 0:
            res = -int(''.join(list(str(0-x))[::-1]))
        if x == 0:
            res = 0
        if res >= pow(2,31) or res < -pow(2,31):
            return 0
        else:
            return res
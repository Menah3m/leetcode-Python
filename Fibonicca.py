# Name:Fibonicca
# Author:Yasu
# Time:2020/3/18

class Solution(object):
    def fib(self, n):
        """
        :type n: int
        :rtype: int
        """
        res = [0,1,1]

        while len(res) <= n:
            res.append(res[-1]+res[-2])
        return (res[n]%(1000000007))  ##leetcode 官方提交需要取模
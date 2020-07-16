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




'''这里的fib是一个生成器generator'''
def fib(n):
    x, a, b = 0, 1, 1
    while x < n:
        yield b
        a, b = b, a+b
        x+=1
    return 'done'


"""使用递归实现 """
class Solution:
    def fib(self, N: int) -> int:
        cache = {}
        def recur_fib(N):
            if N in cache:
                return cache[N]
            if N < 2:
                result = N
            else:
                result = recur_fib(N-1) + recur_fib(N-2)
            return result
        return recur_fib(N)
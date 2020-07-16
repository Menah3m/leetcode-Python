"""
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.
给定 N，计算 F(N)。

 

示例 1：

输入：2
输出：1
解释：F(2) = F(1) + F(0) = 1 + 0 = 1.
示例 2：

输入：3
输出：2
解释：F(3) = F(2) + F(1) = 1 + 1 = 2.
示例 3：

输入：4
输出：3
解释：F(4) = F(3) + F(2) = 2 + 1 = 3.

来源：LeetCode
链接：https://leetcode-cn.com/problems/fibonacci-number

"""
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




'''生成器generator实现'''
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


"""
使用记忆化实现
"""
class Solution:
    def fib(self, N: int) -> int:
        a, b = 0, 1
        if N == 0: return a
        if N == 1: return b
        
        while N > 1:
            a, b = b, a+b
            N -= 1
        return b

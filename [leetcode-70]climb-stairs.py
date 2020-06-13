
"""
假设你正在爬楼梯。需要 n 阶你才能到达楼顶。

每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？

注意：给定 n 是一个正整数。

示例 1：

输入： 2
输出： 2
解释： 有两种方法可以爬到楼顶。
1.  1 阶 + 1 阶
2.  2 阶
示例 2：

输入： 3
输出： 3
解释： 有三种方法可以爬到楼顶。
1.  1 阶 + 1 阶 + 1 阶
2.  1 阶 + 2 阶
3.  2 阶 + 1 阶

来源：LeetCode-70
链接：https://leetcode-cn.com/problems/climbing-stairs


"""
class Solution:
    def climbStairs(self, n: int) -> int:
        if n < 2:
            return n
        temp = [2,3]
        if n < 4:
            return temp[n-2]
        while n > 3:
            res =  temp[0] + temp[1]
            temp[0] = temp[1]
            temp[1] = res
            n -= 1
        return res
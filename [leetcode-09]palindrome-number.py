"""
判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

示例 1:

输入: 121
输出: true
示例 2:

输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
示例 3:

输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
进阶:

你能不将整数转为字符串来解决这个问题吗？

来源：LeetCode-09
链接：https://leetcode-cn.com/problems/palindrome-number

"""
### 转字符串
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x >= 0 and str(x)==str(x)[::-1]


### 不转字符串
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res, temp = 0, x
        while temp:
            res = res*10 + temp%10
            temp //= 10
        return res == x
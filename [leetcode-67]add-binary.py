"""
给你两个二进制字符串，返回它们的和（用二进制表示）。

输入为 非空 字符串且只包含数字 1 和 0。

 

示例 1:

输入: a = "11", b = "1"
输出: "100"
示例 2:

输入: a = "1010", b = "1011"
输出: "10101"

来源：LeetCode-67
链接：https://leetcode-cn.com/problems/add-binary
"""

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a, b = int(a, 2), int(b, 2)
        while b:
            ans = a ^ b
            carr = (a & b) << 1
            a, b = ans, carr
        return bin(a)[2:]
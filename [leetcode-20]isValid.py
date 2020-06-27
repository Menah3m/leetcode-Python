"""
给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

输入: "()"
输出: true
示例 2:

输入: "()[]{}"
输出: true
示例 3:

输入: "(]"
输出: false
示例 4:

输入: "([)]"
输出: false
示例 5:

输入: "{[]}"
输出: true

来源：LeetCode-20
链接：https://leetcode-cn.com/problems/valid-parentheses

"""






class Solution:
    def isValid(self, s: str) -> bool:
        '''思路：用栈的思想，
           如果是左括号，直接入栈，
           如果是右括号，则需要和栈顶元素比较，匹配的上则将栈顶元素推出去，匹配不上则为无效括号
           如果一开始就是右括号，则为无效括号'''
        stack = []     //创建堆栈
        parent_map = {')':'(', ']':'[', '}':'{'}   //创建筛选字典
        if len(s) % 2 != 0:                        //先判断长度，奇数则必定为无效括号
            return False
        for c in s:              
            if c not in parent_map:
                stack.append(c)
            elif not stack or parent_map[c] != stack.pop():  //这里 比较和推出 时实现了
                return False
        return not stack                                     // 最后栈为空则说明全部都配对了

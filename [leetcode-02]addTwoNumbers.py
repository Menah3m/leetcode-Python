"""
给出两个 非空 的链表用来表示两个非负的整数。其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。

如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。

您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

示例：

输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 0 -> 8
原因：342 + 465 = 807

来源：LeetCode-02
链接：https://leetcode-cn.com/problems/add-two-numbers
"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def convert(List):
            num = ''
            while List != None:
                num = str(List.val) + num
                List = List.next
            return int(num)

        num1, num2 = convert(l1), convert(l2)
        num = num1 + num2

        res = ListNode(num % 10)
        l3 = res
        num = num // 10
        while num != 0:
            l3.next = ListNode(num % 10)
            l3 = l3.next
            num = num // 10

        return res
'''
思路1：
将链表转换为数字，相加后再转换为链表
'''
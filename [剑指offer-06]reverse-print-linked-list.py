"""
输入一个链表的头节点，从尾到头反过来返回每个节点的值（用数组返回）。

 

示例 1：

输入：head = [1,3,2]
输出：[2,3,1]
 

限制：

0 <= 链表长度 <= 10000


链接：https://leetcode-cn.com/leetbook/read/illustrate-lcof/xs92sh/
来源：剑指offer-06

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reversePrint(self, head: ListNode) -> List[int]:
        if not head:
            return []
        res = [head.val]
        while head.next:
            res.append(head.next.val)
            head = head.next
        res = res[::-1]
        return res
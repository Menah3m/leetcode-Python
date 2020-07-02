# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

"""
剑指offer-24题
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
"""
"""
leetcode-206
反转一个单链表。

示例:

输入: 1->2->3->4->5->NULL
输出: 5->4->3->2->1->NULL
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = None
        cur = head
        while cur != None:
            tmp = cur.next //先保存当前节点的下一个值
            cur.next = pre //确定原来的前一节点为下一节点
            pre = cur      // pre 移动
            cur = tmp      // cur 移动
        return pre         // 原来的末尾节点是新链表的头节点
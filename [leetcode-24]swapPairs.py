'''
leetcode-24
给定一个链表，两两交换其中相邻的节点，并返回交换后的链表。
你不能只是单纯的改变节点内部的值，而是需要实际的进行节点交换。

'''




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

###递归
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head

        re = head.next
        head.next = self.swapPairs(head.next.next)
        re.next = head

        return re


### 非递归
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        virtual = ListNode(1)
        virtual.next = head
        cur = virtual
        while cur.next and cur.next.next:
            a, b = cur.next, cur.next.next
            cur.next, a.next = b, b.next
            b.next = a
            cur = cur.next.next
        return virtual.next
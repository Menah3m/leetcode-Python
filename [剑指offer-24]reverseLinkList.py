# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

'''
剑指offer-24题
定义一个函数，输入一个链表的头节点，反转该链表并输出反转后链表的头节点。
'''

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next: return head

        Last = None               //Last代表当前指针的上一个，初始值为空
        
        while head:
            tmp = head.next       
            head.next = Last
            Last = head
            head = tmp

        return Last


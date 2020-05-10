# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
'''
给定一个链表，判断链表中是否有环。

为了表示给定链表中的环，我们使用整数 pos 来表示链表尾连接到链表中的位置（索引从 0 开始）。 如果 pos 是 -1，则在该链表中没有环。

来源：LeetCode-141
链接：https://leetcode-cn.com/problems/linked-list-cycle

'''

# 快慢指针法
class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if not head or not head.next: return False

        slow = head
        quick = head
        while slow and quick:
            slow = slow.next
            if quick.next:
                quick = quick.next.next
            else:
                return False
            
            if slow is quick:
                return True
        return False
            
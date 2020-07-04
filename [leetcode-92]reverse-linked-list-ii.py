"""
反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

说明:
1 ≤ m ≤ n ≤ 链表长度。

示例:

输入: 1->2->3->4->5->NULL, m = 2, n = 4
输出: 1->4->3->2->5->NULL

来源：LeetCode-92
链接：https://leetcode-cn.com/problems/reverse-linked-list-ii

"""



# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if not head or not head.next:
            return head
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = dummy_head
        pre = None
        for _ in range(m):
            pre = cur
            cur = cur.next
        
        front = cur
        temp = None
        pre_temp = None
        for _ in range(n-m+1):
            temp = cur.next
            cur.next = pre_temp
            pre_temp= cur
            cur = temp

        pre.next = pre_temp
        front.next = temp
        return dummy_head.next

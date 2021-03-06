"""
给定一个排序链表，删除所有重复的元素，使得每个元素只出现一次。

示例 1:

输入: 1->1->2
输出: 1->2
示例 2:

输入: 1->1->2->3->3
输出: 1->2->3

来源：LeetCode-83
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        pre = head
        cur = head.next
        while cur != None:
            if pre.val == cur.val:
                pre.next = cur.next
                cur = cur.next
            else:
                cur = cur.next
                pre = pre.next
        return head
            
        
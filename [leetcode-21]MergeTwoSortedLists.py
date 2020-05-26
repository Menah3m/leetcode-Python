'''
将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：

输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4

来源：LeetCode-21
链接：https://leetcode-cn.com/problems/merge-two-sorted-lists


'''


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        def recursive(ln1, ln2):
            if not ln1:
                return ln2
            if not ln2:
                return ln1
            if ln1.val < ln2.val:
                ln1.next = recursive(ln1.next, ln2)
                return ln1
            else:
                ln2.next = recursive(ln2.next, ln1)
                return ln2
        return recursive(l1, l2)
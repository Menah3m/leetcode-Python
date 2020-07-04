"""
给定一个排序链表，删除所有含有重复数字的节点，只保留原始链表中 没有重复出现 的数字。

示例 1:

输入: 1->2->3->3->4->4->5
输出: 1->2->5
示例 2:

输入: 1->1->1->2->3
输出: 2->3

来源：LeetCode-82
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-list-ii

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
        dummy_head = ListNode(0)
        dummy_head.next = head
        cur = head
        pre = dummy_head
        while cur:
            cur_val = cur.val
            is_dup = False     // flag:判断当前节点是否为重复值
            while cur.next:    // 往下遍历，如果重复，则跳过该节点
                if cur.next.val == cur_val:
                    cur = cur.next
                    is_dup = True    // flag置为1
                else:
                    break         //若不重复，则结束该次遍历
            if is_dup:            //若为重复元素，则删除节点
                pre.next = cur.next
            else:
                pre = cur 
            cur = cur.next
        return dummy_head.next


"""
给定一个链表和一个特定值 x，对链表进行分隔，使得所有小于 x 的节点都在大于或等于 x 的节点之前。

你应当保留两个分区中每个节点的初始相对位置。

示例:

输入: head = 1->4->3->2->5->2, x = 3
输出: 1->2->2->4->3->5

来源：LeetCode-86
链接：https://leetcode-cn.com/problems/partition-list


"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    """思路：拿出比目标值大的数组成新链表，然后拼接到原链表尾部"""
    def partition(self, head: ListNode, x: int) -> ListNode:
        if not head or not head.next:
            return head
        head_dummy = ListNode(0) // 整个链表的虚拟头节点
        tail_dummy = ListNode(0) //用于存放比目标值大的值的虚拟链表头
        head_dummy.next = head
        tail = tail_dummy    // 用于存放比目标值大的值的链表
        cur = head_dummy
        while cur.next != None:
            if cur.next.val >= x:
                t = cur.next
                cur.next = cur.next.next
                tail.next = t
                tail = tail.next
            else:
                cur = cur.next
        tail.next = None      // 确定尾节点（没有这步会超出时间限制） 
        cur.next = tail_dummy.next // 拼接两个链表
        return head_dummy.next
            

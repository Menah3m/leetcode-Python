
'''
给定一个链表，删除链表的倒数第 n 个节点，并且返回链表的头结点。

示例：

给定一个链表: 1->2->3->4->5, 和 n = 2.

当删除了倒数第二个节点后，链表变为 1->2->3->5.
说明：

给定的 n 保证是有效的。

进阶：

你能尝试使用一趟扫描实现吗？

来源：LeetCode-19
链接：https://leetcode-cn.com/problems/remove-nth-node-from-end-of-list

'''




# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

#思路：1.使用双指针思想，前指针先移动n，然后后指针从头开始，两个指针同时移动，
#        当前指针移动到最后时，将后指针的下一跳指向下下个节点即可
#     2. 边缘情况：要求删除头节点，此时无法直接删除
#        解决方案：设置虚拟头节点，使其指向真正的头节点
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        if not head:
            return head
        virtulhead = l = r = ListNode(10086)
        virtulhead.next = head

        for i in range(n):
            r = r.next 
        while r.next:
            l = l.next
            r = r.next
        l.next = l.next.next

        return virtulhead.next
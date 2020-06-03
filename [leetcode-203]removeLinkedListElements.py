'''
leetcode-203

删除链表中等于给定值 val 的所有节点。

示例:

输入: 1->2->6->3->4->5->6, val = 6
输出: 1->2->3->4->5
'''





# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        virtualhead = ListNode(1)
        virtualhead.next = head
        cur = head
        pre = virtualhead

        while cur != None:
            if cur.val == val:
                cur = cur.next
                pre.next = cur                
            else:
                pre, cur = cur, cur.next
 
        return virtualhead.next
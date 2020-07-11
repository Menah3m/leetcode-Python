"""
给你一个链表，每 k 个节点一组进行翻转，请你返回翻转后的链表。

k 是一个正整数，它的值小于或等于链表的长度。

如果节点总数不是 k 的整数倍，那么请将最后剩余的节点保持原有顺序。

 

示例：

给你这个链表：1->2->3->4->5

当 k = 2 时，应当返回: 2->1->4->3->5

当 k = 3 时，应当返回: 3->2->1->4->5

 

说明：

你的算法只能使用常数的额外空间。
你不能只是单纯的改变节点内部的值，而是需要实际进行节点交换。

来源：LeetCode-25
链接：https://leetcode-cn.com/problems/reverse-nodes-in-k-group

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummy = ListNode(0)
        dummy.next = head
        end = prev = dummy
        def swap(prev, k, end):#prev为原链表的头节点，end为分组的最后一个节点
            after = end.next  #after为分组最后一个节点的下一个节点
            move = prev.next  #move为分组的第一个节点
            prev.next = end
            temp = move.next
            end = move
            for i in range(k-1):
                tnext = temp.next
                temp.next = move
                move = temp
                temp = tnext
            end.next = after
            return end
        
        while True:
            try:
                for _ in range(k):
                    end = end.next
                prev = end = swap(prev, k, end)
            except:
                break
        return dummy.next
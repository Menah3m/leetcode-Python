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
        pre = None      //pre用于保存第一个断点的前一个节点
        for _ in range(m):
            pre = cur
            cur = cur.next
        
        back = cur      // 该节点为反转后的末尾节点（反转前的m位置的节点）
        temp = None     //用于存放反转时的下一个节点
        pre_temp = None //用于存放反转后的最后一个节点（反转前指向m位置的节点）
        for _ in range(n-m+1):
            temp = cur.next
            cur.next = pre_temp
            pre_temp= cur
            cur = temp

        pre.next = pre_temp  //将第一段和反转后的头节点相连
        back.next = temp    
        return dummy_head.next

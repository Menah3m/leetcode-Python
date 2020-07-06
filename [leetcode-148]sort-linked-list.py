"""
在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序。

示例 1:

输入: 4->2->1->3
输出: 1->2->3->4
示例 2:

输入: -1->5->3->4->0
输出: -1->0->3->4->5

来源：LeetCode-148
链接：https://leetcode-cn.com/problems/sort-list

"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        slow, fast = head, head.next    #设置快慢指针
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next
        mid, slow.next = slow.next, None      #从中间将链表切割（slow.next=None）
        left, right = self.sortList(head), self.sortList(mid)   #递归分割
        h = res = ListNode(0)                 #是指头节点来接收合并后的结果
        while left and right:                 #使用left和right两个指针进行结果的合并
            if left.val < right.val:
                h.next, left = left, left.next
            else:
                h.next, right = right, right.next
            h = h.next
        h.next = left if left else right     #最后一个节点的判断
        return res.next                      #返回结果
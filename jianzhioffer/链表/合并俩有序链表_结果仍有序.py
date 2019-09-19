#coding=utf-8
# 合并两个排序链表,使结果依然有序.


# 非递归版  牛客ac
# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution(object):
    def mergeTwoLists(self, pHead1, pHead2):
        tmp = ListNode(0)
        phead = tmp
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                tmp.next = pHead1
                pHead1 = pHead1.next
            else:
                tmp.next = pHead2
                pHead2 = pHead2.next
            tmp = tmp.next
        if pHead1:
            tmp.next = pHead1
        if pHead2:
            tmp.next = pHead2
        return phead.next






# -*- coding:utf-8 -*-
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
# 递归  牛客ac
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # 1 或者 2 为空的话，直接返回另一个链表无需merge
        if not pHead1:
            return pHead2
        if not pHead2:
            return pHead1
        if pHead1.val < pHead2.val:
            prenew = pHead1
            prenew.next = self.Merge(pHead1.next, pHead2)
        else:
            prenew = pHead2
            prenew.next = self.Merge(pHead1, pHead2.next)
        return prenew




# # test
# head1 = ListNode(1)
# p1 = ListNode(3)  # 建立链表1->3->5->7->None
# p2 = ListNode(5)
# p3 = ListNode(7)
# head1.next = p1
# p1.next = p2
# p2.next = p3

# head2 = ListNode(2)
# p12 = ListNode(4)  # 建立链表2->4->6->8->None
# p22 = ListNode(6)
# p32 = ListNode(8)
# head2.next = p12
# p12.next = p22
# p22.next = p32


# s = ListNode(0)
# p = s.merge(head1, head2)
# while p:
#     print p.val
#     p = p.next








"""
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        if l1 == None:
            return l2
        if l2 == None:
            return l1
        flag = 0
        res = ListNode(0)
        p = res
        while l1 or l2 or flag:
            if l1 and l2:
                p.next = ListNode((l1.val + l2.val + flag) % 10)
                flag = (l1.val + l2.val + flag) / 10
                l1 = l1.next
                l2 = l2.next
                p = p.next
            elif l1:
                p.next = ListNode((l1.val + flag) % 10)
                flag = (l1.val + flag) / 10
                l1 = l1.next
                p = p.next
            elif l2:
                p.next = ListNode((l2.val + flag) % 10)
                flag = (l2.val + flag) / 10
                l2 = l2.next
                p = p.next
            else:
                p.next = ListNode(flag)
                flag = 0
                p = p.next
        return res.next

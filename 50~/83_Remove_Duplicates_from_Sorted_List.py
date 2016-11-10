"""
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
"""


# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        res = ListNode(0)
        res.next = head
        p = res
        q = head

        while q != None:
            while q.next and q.next.val == p.next.val:
                q = q.next
            p.next = q
            p = p.next
            q = q.next

        return res.next

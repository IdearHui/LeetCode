# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        elif not l2:
            return l1
        lm = ListNode(0)
        if l1.val < l2.val:
            lm = l1
            lm.next = self.mergeTwoLists(l1.next, l2)
        elif l1.val > l2.val:
            lm = l2
            lm.next = self.mergeTwoLists(l1, l2.next)
        return lm

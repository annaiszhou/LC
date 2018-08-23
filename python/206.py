# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head
        cur = head
        nxt = None
        while cur:
            temp = cur.next
            cur.next = nxt
            nxt = cur
            cur = temp
        return nxt

#Runtime: 28 ms
#Your runtime beats 76.09 % of python submissions.
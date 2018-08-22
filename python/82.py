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
        if not head:
        	return head

        dummy = ListNode(0)
        dummy.next = head
        cur = dummy
        value = 0
        while cur.next and cur.next.next:
        	if cur.next.val == cur.next.next.val:
        		value = cur.next.val
        		while cur.next and cur.next.val == value:
        			cur.next = cur.next.next
        	else:
        		cur = cur.next
        return dummy.next

#Runtime: 32 ms
#Your runtime beats 72.70 % of python submissions.

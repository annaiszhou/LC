# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
        	return head
        cur = head
        while cur:
        	while cur.next and cur.val == cur.next.val:
        		cur.next = cur.next.next
        	cur = cur.next
        return head

#Runtime: 68 ms
#Your runtime beats 17.98 % of python3 submissions.


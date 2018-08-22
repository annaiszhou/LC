"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: A ListNode
    @return: A ListNode
    """
    def deleteDuplicates(self, head):
    	if not head:
    		return head
    	cur = head
    	while cur:
    		check = cur
    		while check.next:
    			if check.next.val==cur.val:
    				check.next == ckeck.next.next
    			else:
    				check = check.next
    		cur = cur.next
    	return head

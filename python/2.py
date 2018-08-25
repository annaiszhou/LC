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
        if not l1 or not l2:
        	return l1 or l2
        c = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 is not None or l2 is not None or c>0:
        	if l1 is not None:
        		c = l1.val+c
        		l1 = l1.next
        	if l2 is not None:
        		c = l2.val+c
        		l2 = l2.next
        	cur.next = ListNode(c%10)
        	c = c // 10
        	cur = cur.next 
        return dummy.next

#Runtime: 84 ms
#Your runtime beats 31.94 % of python submissions.

'''
        if not l1 or not l2:
        	return l1 or l2
        c = 0
        dummy = ListNode(0)
        cur = dummy
        while l1 or l2 or c:
        	if l1:
        		c = l1.val+c
        		l1 = l1.next
        	if l2:
        		c = l2.val+c
        		l2 = l2.next
        	cur.next = ListNode(c%10)
        	c = c // 10
        	cur = cur.next 
        return dummy.next

        #Runtime: 68 ms
        #Your runtime beats 95.43 % of python submissions.
'''

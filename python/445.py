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
        def getLength(node):
        	l = 0
        	while node:
        		l += 1
        		node = node.next
        	return l

        def addLeadingZeros(n, node):
        	for i in range(n):
        		new = ListNode(0)
        		new.next = node
        		node = new
        	return node

        def combineList(l1, l2):
        	if (not l1 and not l2):
        		return (0, None)
        	c, new = combineList(l1.next, l2.next)
        	s = l1.val+l2.val+c
        	res = ListNode(s%10)
        	res.next = new
        	return (s/10, res)

        len1, len2 = getLength(l1), getLength(l2)
        l1 = addLeadingZeros(len2-len1, l1)
        l2 = addLeadingZeros(len1-len2, l2)
        c, res = combineList(l1, l2)
        if c>0:
        	l3 = ListNode(c)
        	l3.next = res
        	res = l3
        return res

#Runtime: 72 ms
#Your runtime beats 88.02 % of python submissions.
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        #two pointers
        slow = head
        fast = head
        while(fast != None and fast.next != None):
            slow = slow.next
            fast = fast.next.next
            if(id(slow) == id(fast)):
                return True
        return False
        '''
        #one pointer
        if not head:
            return False
        node = head
        prev = None
        while node:
            _next = node.next
            node.next = prev
            prev = node
            node = _next
            if node is head:
                return True
            
        return False
        '''

#Runtime: 48 ms
#Your runtime beats 94.56 % of python submissions.
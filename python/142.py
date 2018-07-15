# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        size = self.CycleSize(head)
        if size:
            p = head
            q = head
            for i in range(size):
                q = q.next
            while p!=q:
                p=p.next
                q=q.next
            return p
        return None

    def CycleSize(self, head):
        p = head
        q = head
        while q and q.next:
            p = p.next
            q = q.next.next
            if q == p:
                size = 0
                while True:
                    q = q.next
                    size += 1
                    if q == p:
                        break
                return size
        return 0

#Runtime: 44 ms
#Your runtime beats 100.00 % of python submissions.
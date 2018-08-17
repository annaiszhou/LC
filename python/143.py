# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: void Do not return anything, modify head in-place instead.
        """
        while head is None:
            return head
        neg = -1
        pos = 1
        dummy = ListNode(0)
        dummy.next = head
        res = dummy.next
        nums = []
        while head:
            nums.append(head.val)
            head = head.next
        head = dummy.next
        for i in range(len(nums)):
            if i ==0:
                continue
            if i % 2 == 0:
                head.next = ListNode(nums[pos])
                pos +=1
                head = head.next
            else:
                head.next = ListNode(nums[neg])
                neg -= 1
                head = head.next
        head.next = None

#Runtime: 228 ms
#Your runtime beats 3.11 % of python submissions.
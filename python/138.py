# Definition for singly-linked list with a random pointer.
# class RandomListNode(object):
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: RandomListNode
        :rtype: RandomListNode
        """
        map = {}
        iterNode = head
        while iterNode:
            map[iterNode] = RandomListNode(iterNode.label)
            iterNode = iterNode.next
        iterNode = head
        while iterNode:
            map[iterNode].next = map[iterNode.next] if iterNode.next else None
            map[iterNode].random = map[iterNode.random] if iterNode.random else None
            iterNode = iterNode.next
        return map[head] if head else None

#Runtime: 72 ms
#Your runtime beats 85.01 % of python submissions.
class Node(object):
    def __init__(self, k, v):
        self.prev = None
        self.next = None
        self.key = k
        self.val = v
        self.cnt = 1

class DoublyLinkedList(object):
    def __init__(self):
        self.head = Node(0, 0) # head is a dummy head node
        self.tail = Node(0, 0) # tail is a dummy tail node
        self.head.next = self.tail
        self.tail.prev = self.head
        self.size = 0

    def add_to_head(self, node):
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
        node.prev = self.head
        self.size += 1

    def remove_tail(self):
        old_tail = self.tail.prev
        node = self.tail.prev
        node.prev.next = self.tail
        self.tail.prev = node.prev
        self.size -= 1
        return old_tail

    def remove_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        self.size -= 1

class LFUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.node_dict = {}
        self.freq_dict = collections.defaultdict(DoublyLinkedList)
        self.capacity = capacity
        self.size = 0
        self.min_freq = 0

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key not in self.node_dict:
            return -1
        else:
            node = self.node_dict[key]
            old_cnt = node.cnt
            node.cnt += 1
            self.freq_dict[old_cnt].remove_node(node)
            self.freq_dict[node.cnt].add_to_head(node)
            if old_cnt == self.min_freq and self.freq_dict[old_cnt].size == 0:
                self.min_freq += 1
            return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if self.capacity <= 0:
            return
        if key not in self.node_dict:
            node = Node(key, value)
            self.node_dict[key] = node
            if self.size != self.capacity:
                self.freq_dict[1].add_to_head(node)
                self.size += 1
            else:
                old_tail = self.freq_dict[self.min_freq].remove_tail()
                self.node_dict.pop(old_tail.key)
                self.freq_dict[1].add_to_head(node)
            self.min_freq = 1
        else:
            node = self.node_dict[key]
            node.val = value
            old_cnt = node.cnt
            node.cnt += 1
            self.freq_dict[old_cnt].remove_node(node)
            self.freq_dict[node.cnt].add_to_head(node)
            if old_cnt == self.min_freq and self.freq_dict[old_cnt].size == 0:
                self.min_freq += 1

# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#Runtime: 156 ms
#Your runtime beats 91.16 % of python submissions.
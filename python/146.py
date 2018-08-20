class LRUCache(object):
    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.n_items = 0
        self.cache = dict()
        self.LRU = collections.deque() 

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        if key in self.cache:
            self.LRU.remove(key)
            self.LRU.appendleft(key)
            return self.cache[key]
        else:
            return -1

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: void
        """
        if key not in self.cache:
            if self.n_items < self.capacity:
                self.n_items += 1
                self.LRU.appendleft(key)
                self.cache[key] = value
            else:
                key2remove = self.LRU.pop()
                del self.cache[key2remove]
                self.LRU.appendleft(key)
                self.cache[key] = value
        else:
            self.LRU.remove(key)
            self.LRU.appendleft(key)
            self.cache[key] = value

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

#Runtime: 624 ms
#Your runtime beats 9.24 % of python submissions.
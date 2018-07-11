class MinStack(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.min=[]
        self.stack=[]
        
    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if not self.min or x <= self.min[-1]:
            self.min.append(x)
        self.stack.append(x)
        
    def pop(self):
        """
        :rtype: void
        """
        if not self.stack:
            return 
        if self.stack[-1] == self.min[-1]:
            self.min.pop()
        self.stack.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]
        
    def getMin(self):
        """
        :rtype: int
        """
        if not self.min:
            return 
        return self.min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#Runtime: 56 ms
#Your runtime beats 100.00 % of python3 submissions.
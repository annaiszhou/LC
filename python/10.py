class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memory = {}
        return self.helper(s, 0, p, 0, memory)

    def match(self, s, i, p, j):
        if i == len(s) or j == len(p):
            return False
        return p[j] == '.' or s[i] == p[j]
    
    def helper(self, s, i, p, j, memory):
        if j == len(p):
            return i == len(s)
        if i > len(s):
            return False
        if (i, j) in memory:
            return memory[(i, j)]
        if j < len(p)-1 and p[j+1] == '*':
            memory[(i, j)] = (self.match(s, i, p, j) and self.helper(s, i+1, p, j, memory)) or self.helper(s, i, p, j+2, memory)
            return memory[(i, j)]
        if self.match(s, i, p, j):
            memory[(i, j)] = self.helper(s, i+1, p, j+1, memory)
            return memory[(i, j)] 
        return False

#Runtime: 36 ms
#Your runtime beats 99.78 % of python submissions.
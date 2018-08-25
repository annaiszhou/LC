class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if not s:
            return [""]
        self.solution_found = False
        self.visited_potential_solutions = set()
        self.results = set()
        self.bfs(s)
        return list(self.results)

    def bfs(self, s):
        if s is "" or s is None:
            return 
        stack = []
        stack.append(s)        
        while stack:
            current = stack.pop(0)
            if self.is_valid(current):
                self.solution_found = True
                self.results.add(current)
                continue
            if self.solution_found:
                continue
            for i,c in enumerate(current):
                if not self.is_parenthesis(c):
                    continue
                potential_solution = current[:i]+current[i+1:]
                if potential_solution not in self.visited_potential_solutions:
                    self.visited_potential_solutions.add(potential_solution)
                    stack.append(potential_solution)
    
    def is_valid(self, s):
        left_and_right = 0
        for c in s:
            if c == '(':
                left_and_right += 1
            if c == ')':
                left_and_right -= 1
                if left_and_right < 0:
                    return False
        return left_and_right == 0

    def is_parenthesis(self, c):
        return c in ['(', ')']

#Runtime: 260 ms
#Your runtime beats 37.34 % of python3 submissions.
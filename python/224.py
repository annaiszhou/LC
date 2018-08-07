class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        res, operator, current, stack = 0, 1, 0, []
        for character in s:
            if character == ' ':
                continue
            elif character.isdigit():
                current = current*10 + int(character)
            elif character == '(':
                stack.append(res)
                stack.append(operator)
                operator, res = 1, 0
            elif character == '+':
                res += operator*current
                current = 0
                operator = 1
            elif character == '-':
                res += operator*current
                current, operator = 0, -1
            elif character == ')':
                res += current*operator
                res *= stack.pop()
                res += stack.pop()
                current = 0
        if current:
            res += current*operator
        return res

#Runtime: 144 ms
#Your runtime beats 68.10 % of python submissions.
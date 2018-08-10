class Solution:
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        def signum(x):
            return -1 if x < 0 else 1

        operation = {'+', '-', '/', '*'}
        nums = []
        for ch in tokens:
            if ch not in operation:
                nums.append(int(ch))
                continue
            b, a = nums.pop(), nums.pop()
            if ch == '+':
                c = a+b
            elif ch == '-':
                c = a-b
            elif ch == '/':
                c = signum(a)*signum(b)*(abs(a)//abs(b))
            elif ch == '*':
                c = a*b
            else:
                raise ValueError(ch)
            nums.append(c)
        return nums.pop()

#Runtime: 40 ms
#Your runtime beats 83.86 % of python submissions.
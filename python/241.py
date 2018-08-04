class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        def operate(a, x, b):
            if x == "+":
                return a + b
            if x == "-":
                return a - b
            if x == "*":
                return a * b

        def helper(A):
            if len(A) == 1:
                return A
            if len(A) == 3:
                return [operate(A[0],A[1],A[2])]
            result = []
            for position in range(1, len(A), 2):
                x = A[:position]
                y = A[position+1:]
                for i in helper(x):
                    for j in helper(y):
                        result.append(operate(i, A[position], j))
            return result

        source = []
        origin = ""
        for s in input:
            if s == "+" or s == "-" or s == "*":
                source.append(int(origin))
                source.append(s)
                origin = ""
            else:
                origin+=s
        source.append(int(origin))
        res = helper(source) 
        return res

#Runtime: 28 ms
#Your runtime beats 78.72 % of python submissions.
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if not n:
        	return []
        
        def helper(left,right,s):
        	if left==right==n:
        		res.append(''.join(s))
        		return
        	if left<n:
        		s.append('(')
        		helper(left+1,right,s)
        		s.pop()
        	if right<left:
        		s.append(')')
        		helper(left,right+1,s)
        		s.pop()

        res = []
        helper(0,0,[])
        return res

#Runtime: 32 ms
#Your runtime beats 31.29 % of python submissions.







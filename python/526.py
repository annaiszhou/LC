class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """
        def helper(nums,arrangements):
        	global res
        	if nums>N:
        		res+=1
        	else:
        		for a in arrangements:
        			if a%nums == 0 or nums%a == 0:
        				arrangements.remove(a)
        				helper(nums+1,arrangements)
        				arrangements.add(a)

        global res
        res = 0
        arrangement = set(i+1 for i in range(N))
        helper(1,arrangement)
        return res

#Runtime: 860 ms
#Your runtime beats 45.72 % of python submissions.
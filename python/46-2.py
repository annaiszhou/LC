class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
        	return []
        res = []
        path = []
        status = ['False']*len(nums)
        
        def helper(i,nums):
        	if i==len(nums):
        		#print (path)
        		res.append(copy.deepcopy(path))
        		#print (res)
        		return
        	for j in range(len(nums)):
        		if status[j]=='False':
        			status[j] = 'True'
        			path.append(nums[j])
        			helper(i+1,nums)
        			status[j] = 'False'
        			path.pop()

        helper(0,nums)
        return res

#Runtime: 64 ms
#Your runtime beats 21.99 % of python3 submissions.

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if k == 0: 
        	return any(a==b==0 for a, b in zip(nums, nums[1:]))
        k = abs(k)
        reminder, reminders = 0, {0: -1}
        for i, v in enumerate(nums):
            reminder = (reminder + v) % k
            j = reminders.get(reminder)
            if j == None:
            	reminders[reminder] = i
            elif i - j >= 2:
                return True
        return False

#Runtime: 32 ms
#Your runtime beats 76.98 % of python submissions.
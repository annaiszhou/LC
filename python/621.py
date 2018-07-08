class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        task_count={}
        for task in set(tasks):
        	task_count[task]=tasks.count(task)
        max_count=max(task_count.values())
        max_num=len([task for task in task_count if task_count[task] == max_count])
        return max(len(tasks),(max_count-1)*(n+1)+max_num)

#Runtime: 84 ms
#Your runtime beats 65.44 % of python3 submissions.
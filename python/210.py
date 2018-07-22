class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        course = [[] for numCourse in range(numCourses)]
        for prerequisite in prerequisites:
            course[prerequisite[1]].append(prerequisite[0])

        res = []
        state = [1] * numCourses

        for i in range(numCourses):
            if state[i] == 3:
                continue
            s = [i]
            while len(s) > 0:
                cur = s.pop()
                if state[cur] == 3:
                    continue
                elif state[cur] == 1:
                    state[cur] = 2
                elif state[cur] == 2:
                    state[cur] = 3
                    res.append(cur)
                    continue
                s.append(cur)
                for next_course in course[cur]:
                    if state[next_course] == 2:
                        return []
                    s.append(next_course)
        return res[::-1]

#Runtime: 40 ms
#Your runtime beats 77.10 % of python submissions.
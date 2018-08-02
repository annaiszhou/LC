class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]
        targetA = [0] * 26
        for x in A:
            targetA[x] += 1
        targetB = [0] * 26
        for i, x in enumerate(B):
            targetB[x] += 1
            if i >= len(A):
                targetB[B[i - len(A)]] -= 1
            if targetB == targetA:
                return True
        return False

#Runtime: 56 ms
#Your runtime beats 66.20 % of python submissions.
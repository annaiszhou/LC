class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        if not word1 or not word2:
            return len(word1)+len(word2)

        dp=[[0 for col in range(len(word2)+1)] for row in range(len(word1)+1)]
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                if i==0 and j==0:
                    continue
                if i==0:
                    dp[i][j]=j
                elif j==0:
                    dp[i][j]=i
                else:
                    if word1[i-1]==word2[j-1]:
                        dp[i][j]+=dp[i-1][j-1]
                    else:
                        dp[i][j]+=min(dp[i-1][j],dp[i-1][j-1],dp[i][j-1])+1
        return dp[-1][-1]

#Runtime: 280 ms
#Your runtime beats 9.47 % of python submissions.
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1 or numRows >= len(s):
            return s
        index , step = 0 , 1
        res = ['']*numRows
        for ss in s:
            res[index] += ss
            if index == 0:
                step = 1
            elif index == numRows-1:
                step = -1
            else:
                None
            index += step
        return ''.join(res)

#Runtime: 68 ms
#Your runtime beats 62.08 % of python submissions.
#space: O(n)
#time: O(n)

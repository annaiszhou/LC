class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if not digits:
            return []
        res = []
        string = []
        map_dict={'2':'abc', '3':'def', '4':'ghi', '5':'jkl', '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

        def helper(i,string,res):
            if i==len(digits):
                res.append(''.join(string))
                return
            for number in map_dict[digits[i]]:
                string.append(number)
                helper(i+1,string,res)
                string.pop()

        helper(0,string,res)
        return res

#Runtime: 56 ms
#Your runtime beats 9.02 % of python3 submissions.
#space: O(4^digits)
#time: O(4^digits)
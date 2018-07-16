class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ""
        while s:
            counts = collections.Counter(s)
            position = 0
            for i , x in enumerate(s):
                if x < s[position]: #lexicographical order
                	position = i
                counts[x] -= 1
                if counts[x] == 0: 
                	break             
            res += s[position]
            s = s[position+1:].replace(s[position], "")
        return res

#Runtime: 132 ms
#Your runtime beats 20.65 % of python submissions.
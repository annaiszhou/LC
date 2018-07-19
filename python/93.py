class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, 0, "", res)
        return res
        
    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1])
            return
        for i in xrange(1, 4):
            if i <= len(s):
                if i == 1: 
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
                elif i == 2 and s[0] != "0": 
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index+1, path+s[:i]+".", res)

#Runtime: 24 ms
#Your runtime beats 100.00 % of python submissions.
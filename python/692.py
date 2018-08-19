class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        d = {}
        for word in words:
            d[word] = d.get(word, 0) + 1
        res = sorted(d, key=lambda word: (-d[word], word))
        return res[:k]

#Runtime: 44 ms
#Your runtime beats 25.49 % of python submissions.
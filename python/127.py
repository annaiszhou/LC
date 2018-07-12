class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        def construct(word_list):
            d = {}
            for word in word_list:
                for i in range(len(word)):
                    s = word[:i] + "_" + word[i+1:]
                    d[s] = d.get(s, []) + [word]
            return d
            
        def bfs(begin, end, worddict):
            queue, visited = collections.deque([(begin, 1)]), set()
            while queue:
                word, steps = queue.popleft()
                if word not in visited:
                    visited.add(word)
                    if word == end:
                        return steps
                    for i in range(len(word)):
                        s = word[:i] + "_" + word[i+1:]
                        change_words = worddict.get(s, [])
                        for change in change_words:
                            if change not in visited:
                                queue.append((change, steps + 1))
            return 0
        
        d = construct(wordList)
        return bfs(beginWord, endWord, d)

#Runtime: 152 ms
#Your runtime beats 78.79 % of python3 submissions.
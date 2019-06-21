# Leetcode 127 Word Ladder:
# https://leetcode.com/problems/word-ladder/

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList:
            return 0
        steps = {word: 0 for word in wordList}
        steps[beginWord] = 1
        queue = collections.deque([beginWord])
        
        while queue:
            word = queue.popleft()
            step = steps[word]
            for i in range(len(word)):
                left = word[:i]
                right = word[i+1:]
                for j in range(26):
                    testword = left + chr(97+j) + right
                    if testword == endWord:
                        return step + 1
                    if testword in steps and steps[testword] == 0:
                        steps[testword] = step + 1
                        queue.append(testword)
        
        return 0
# 269. Alien Dictionary
# https://leetcode.com/problems/alien-dictionary/description/


# Runtime: 32 ms
# Memory Usage: 14 MB
# Your runtime beats 95.69 % of python3 submissions.
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        indegrees, edges = self.get_indegrees_edges(words)
        queue = collections.deque()
        for key in indegrees:
            if indegrees[key] == 0:
                queue.append(key)

        order = ""
        while queue:
            letter = queue.popleft()
            order += letter
            if letter not in edges:
                continue
            for key in edges[letter]:
                indegrees[key] += -1
                if indegrees[key] == 0:
                    queue.append(key)
        
        return order if len(order) == len(indegrees) else ''
            
        
    
    def get_indegrees_edges(self, words):
        chars = set("".join(words))
        edges = {a:set() for a in chars}
        indegrees = {a:0 for a in chars}
        
        for pair in zip(words, words[1:]):
            for s1, s2 in zip(*pair):
                if s1 != s2:
                    if s2 not in edges[s1]:
                        edges[s1].add(s2)
                        indegrees[s2] += 1
                    break

        return indegrees, edges


# 399. Evaluate Division
# https://leetcode.com/problems/evaluate-division/description/


# Runtime: 32 ms
# Memory Usage: 13.3 MB
# Your runtime beats 88.06 % of python3 submissions.
# Your memory usage beats 21.58 % of python3 submissions.
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        

        father = {}

        def findroot(key):
            if father[key][0] == key:
                return key
            root = findroot(father[key][0])
            father[key] = [root, father[key][1] * father[father[key][0]][1]]
            return root
            
        for [a, b] ,v in zip(equations, values):
            if a not in father:
                father[a] = [a, 1.0]
            if b not in father:
                father[b] = [b, 1.0]
            
            # merge
            if findroot(a) != findroot(b):
                father[findroot(b)] = [findroot(a), v * (father[a][1]/father[b][1])]
        
        ans = []
        for a, b in queries:
            if a not in father or b not in father or findroot(a) != findroot(b):
                ans.append(-1.0)
            else:
                ans.append(father[b][1]/father[a][1])
        
        return ans



# Method 2: Floyd-Warshall
# Reference:
# https://leetcode.com/problems/evaluate-division/discuss/88175/9-lines-%22FloydWarshall%22-in-Python
# Runtime: 36 ms
# Memory Usage: 13.1 MB
# Your runtime beats 67.34 % of python3 submissions.
# Your memory usage beats 68.16 % of python3 submissions.

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        
        quot = collections.defaultdict(dict)
        for (a, b), v in zip(equations, values):
            quot[a][a] = quot[b][b] = 1.0
            quot[a][b] = v
            quot[b][a] = 1.0/v
        
        for k, i, j in itertools.permutations(quot,3):
            if k in quot[i] and j in quot[k]:
                quot[i][j] = quot[i][k] * quot[k][j]
        
        return [quot[a].get(b,-1.0) for a, b in queries]

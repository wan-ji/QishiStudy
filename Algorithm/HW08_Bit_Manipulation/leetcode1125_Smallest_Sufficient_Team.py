# 1125. Smallest Sufficient Team
# https://leetcode.com/problems/smallest-sufficient-team/description/


# Runtime: 276 ms
# Memory Usage: 19.9 MB
# Your runtime beats 31.89 % of python submissions.
class Solution(object):
    def smallestSufficientTeam(self, req_skills, people):
        """
        :type req_skills: List[str]
        :type people: List[List[str]]
        :rtype: List[int]
        """
        skillmap = {}
        skillidx = 1
        for skill in req_skills:
            skillmap[skill] = skillidx
            skillidx <<= 1
        
        peopleskills = [0] * len(people)
        for i, p in enumerate(people):
            for skill in p:
                peopleskills[i] |= skillmap.get(skill,0)
        
        dp = {0:[]}
        for i, p in enumerate(peopleskills):
            for skills, persons in dp.items():
                with_i = p | skills
                if with_i == skills:
                    continue
                if with_i not in dp or len(persons) + 1 < len(dp[with_i]):
                    dp[with_i] = persons + [i]
        
        return dp[skillidx-1]
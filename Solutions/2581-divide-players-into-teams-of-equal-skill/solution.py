class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        num_teams = len(skill)/2
        sum_skill = sum(skill)
        if sum_skill % num_teams != 0:
            return -1
        skill_per_team = sum_skill / num_teams
        dic = {}
        for i in skill:
            dic[i] = dic.get(i, 0) + 1
        ret = 0
        for i in skill:
            if dic.get(skill_per_team - i, 0) > 0:
                ret += i * (skill_per_team - i)
                dic[skill_per_team - i] -= 1
            else:
                return -1
        
        return int(ret/2)

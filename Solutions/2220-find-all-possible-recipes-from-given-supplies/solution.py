from collections import defaultdict, deque
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj_matrix = defaultdict(list)
        out_count = defaultdict(int)

        for i in range(len(recipes)):
            for j in ingredients[i]:
                adj_matrix[j].append(recipes[i])
                out_count[recipes[i]] += 1

        ret = []
        available = deque()
        available.extend(supplies)
        while available:
            sup = available.pop()
            for rec in adj_matrix[sup]:
                out_count[rec] -= 1
                if out_count[rec] == 0:
                    ret.append(rec)
                    available.append(rec)
        return ret
        

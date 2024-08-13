class Solution:
    def combinationSum2(self, candidates, target):
        answer = []
        candidates.sort()
        self.backtrack(candidates, target, 0, [], answer)
        return answer

    def backtrack(self, candidates, target, totalIdx, path, answer):
        if target < 0:
            return  # backtracking
        if target == 0:
            answer.append(path)
            return  # end
        for i in range(totalIdx, len(candidates)):
            if i > totalIdx and candidates[i] == candidates[i - 1]:
                continue
            self.backtrack(
                candidates,
                target - candidates[i],
                i + 1,
                path + [candidates[i]],
                answer,
            )

class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        res = []

        for i in range(len(words)):
            # Include the first word or whenever the group alternates
            if not res or groups[res[-1]] != groups[i]:
                res.append(i)

        # Convert index list to word list
        return [words[i] for i in res]

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Convert wordDict to a set for O(1) lookups
        word_set = set(wordDict)
        results = []
        # Start the backtracking process
        self._backtrack(s, word_set, [], results, 0)
        return results

    def _backtrack(
        self,
        s: str,
        word_set: set,
        current_sentence: List[str],
        results: List[str],
        start_index: int,
    ):
        # If we've reached the end of the string, add the current sentence to results
        if start_index == len(s):
            results.append(" ".join(current_sentence))
            return

        # Iterate over possible end indices
        for end_index in range(start_index + 1, len(s) + 1):
            word = s[start_index:end_index]
            # If the word is in the set, proceed with backtracking
            if word in word_set:
                current_sentence.append(word)
                # Recursively call backtrack with the new end index
                self._backtrack(
                    s, word_set, current_sentence, results, end_index
                )
                # Remove the last word to backtrack
                current_sentence.pop()

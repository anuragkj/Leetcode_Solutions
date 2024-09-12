class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        is_allowed = [False] * 26
        for char in allowed:
            is_allowed[ord(char) - ord("a")] = True

        consistent_count = 0
        for word in words:
            is_consistent = True
            for char in word:
                if not is_allowed[ord(char) - ord("a")]:
                    is_consistent = False
                    break
            if is_consistent:
                consistent_count += 1

        return consistent_count

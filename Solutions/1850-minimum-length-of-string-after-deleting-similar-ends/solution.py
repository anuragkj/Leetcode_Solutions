class Solution:
    def minimumLength(self, s: str) -> int:
        begin = 0
        end = len(s) - 1

        # Delete similar ends until the ends differ or they meet in the middle
        while begin < end and s[begin] == s[end]:
            c = s[begin]

            # Delete consecutive occurrences of c from prefix
            while begin <= end and s[begin] == c:
                begin += 1

            # Delete consecutive occurrences of c from suffix
            while end > begin and s[end] == c:
                end -= 1

        # Return the number of remaining characters
        return end - begin + 1

class Solution(object):
    def partitionString(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 1
        seen = set()
        for char in s:
            if char not in seen:
                seen.add(char)
                continue
            seen.clear()
            seen.add(char)
            count +=1
        return count

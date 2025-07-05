class Solution:
    def findLucky(self, arr: List[int]) -> int:
        return max((k for k, v in Counter(arr).items() if k == v), default=-1)

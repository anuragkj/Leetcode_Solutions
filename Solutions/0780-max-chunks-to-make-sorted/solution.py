class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_num, cnt = -1, 0
        for i, num in enumerate(arr):
            max_num = max(num, max_num)
            if i == max_num:
                cnt += 1
        return cnt

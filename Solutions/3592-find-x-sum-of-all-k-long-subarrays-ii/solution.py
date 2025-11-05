class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        freq = defaultdict(int)
        ans = [0] * (n - k + 1)
        for i in range(k):
            freq[nums[i]] += 1
        pairs = sorted((frequent, num) for num, frequent in freq.items())
        start = 0 if x >= len(pairs) else len(pairs) - x
        higher = SortedList(pairs[start:])
        lower = SortedList(pairs[:start]) 
        sh = sum(num * frequent for num, frequent in higher)
        ans[0] = sh
        for m in range(k, n):
            curr = (freq[nums[m]], nums[m])
            freq[nums[m]] += 1
            next = (curr[0] + 1, nums[m])
            if curr in higher:
                higher.remove(curr)
                higher.add(next)
                sh += nums[m]
            elif len(higher) < x:
                higher.add(next)
                sh += next[0] * next[1]
            else:
                lower.discard(curr)
                lower.add(next)
                if lower[-1] > higher[0]:
                    low = higher.pop(0)
                    high = lower.pop(-1)
                    sh += high[0] * high[1] - low[0] * low[1]
                    lower.add(low)
                    higher.add(high)
            m1 = m - k
            curr = (freq[nums[m1]], nums[m1])
            freq[nums[m1]] -= 1
            next = (curr[0] - 1, nums[m1])
            if curr in higher:
                higher.remove(curr)
                higher.add(next)
                sh -= nums[m1]
            else:
                lower.discard(curr)
                lower.add(next)
            if lower and lower[-1] > higher[0]:
                low = higher.pop(0)
                high = lower.pop(-1)
                sh += high[0] * high[1] - low[0] * low[1]
                lower.add(low)
                higher.add(high)
            ans[m1 + 1] = sh
        return ans

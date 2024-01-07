class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        count, memo  = Counter(nums), Counter()  
        diff, res, d = defaultdict(Counter), 0, 0 

        for num in reversed(nums):
            if num in diff:
                res += sum(diff[num].values())

                for dif in diff[num]:
                    if count[(d := num + dif)]: 
                        diff[d][dif] += diff[num][dif] 

            for used in memo:
                d = num + (dif := num - used)  
                if count[d]: diff[d][dif] += memo[used] 

            memo[num]  += 1  
            count[num] -= 1  

        return res

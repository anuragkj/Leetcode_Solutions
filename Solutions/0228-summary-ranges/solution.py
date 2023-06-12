class Solution:
    def summaryRanges(self, nums):
        output = []
        if len(nums) == 0:
            return output
        elif len(nums) == 1:
            output.append(str(nums[0]))
            return output
        else:
            start = 0
            for i in range(1,len(nums)):
                if nums[i]-nums[i-1]>1:
                    if nums[start] == nums[i-1]:
                        output.append(str(str(nums[start])))
                    else:
                        output.append(str(str(nums[start])+"->"+str(nums[i-1])))
                    start = i
            if nums[start] == nums[i]:
                output.append(str(str(nums[start])))
            else:
                output.append(str(str(nums[start])+"->"+str(nums[i])))
            return output

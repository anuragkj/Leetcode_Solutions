class Solution:
    def sortJumbled(self, mapping, nums):
        store_pairs = []

        for i in range(len(nums)):
            # Convert current value to string
            number = str(nums[i])
            formed = ""
            for j in range(len(number)):
                formed = formed + str(mapping[int(number[j])])
            # Store the mapped value.
            mapped_value = int(formed)
            # Push a pair consisting of mapped value and original value's index.
            store_pairs.append((mapped_value, i))

        # Sort the array in non-decreasing order by the first value (default).
        store_pairs.sort()
        answer = []
        for pair in store_pairs:
            answer.append(nums[pair[1]])
        return answer

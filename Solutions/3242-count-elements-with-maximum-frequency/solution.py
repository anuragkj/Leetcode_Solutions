class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        # Find the frequency of each element
        frequencies = {}
        for num in nums:
            if num in frequencies:
                frequencies[num] += 1
            else:
                frequencies[num] = 1

        # Determine the maximum frequency
        max_frequency = 0
        for frequency in frequencies.values():
            max_frequency = max(max_frequency, frequency)

        # Calculate the total frequencies of elements with the maximum frequency
        frequency_of_max_frequency = 0
        for frequency in frequencies.values():
            if frequency == max_frequency:
                frequency_of_max_frequency += 1

        return frequency_of_max_frequency * max_frequency

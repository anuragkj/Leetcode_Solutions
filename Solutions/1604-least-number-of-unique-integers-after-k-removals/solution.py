class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        # Dictionary to track the frequencies of elements
        freq_map = Counter(arr)

        # List to track all the frequencies
        frequencies = list(freq_map.values())

        # Sorting the frequencies
        frequencies.sort()

        # Tracking the number of elements removed
        elements_removed = 0

        for i in range(len(frequencies)):
            # Removing frequencies[i] elements, which equates to
            # removing one unique element
            elements_removed += frequencies[i]

            # If the number of elements removed exceeds k, return
            # the remaining number of unique elements
            if elements_removed > k:
                return len(frequencies) - i

        # We have removed all elements, so no unique integers remain
        # Return 0 in this case
        return 0

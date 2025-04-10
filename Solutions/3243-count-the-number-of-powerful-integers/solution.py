class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, suffix: str) -> int:
        """
        Count the number of powerful integers in the range [start, finish] that satisfy:
          1. The integer ends with the fixed suffix `suffix`.
          2. Every digit of the integer is at most equal to `limit`.
          
        This is done by computing the number of valid numbers <= a given bound and subtracting:
            count_up_to(finish) - count_up_to(start - 1)
        """
        def count_up_to(num_str: str, suffix: str, limit: int) -> int:
            """
            Count how many valid numbers <= num_str (given as a string) meet the powerful integer criteria.
            A valid number:
              - Has all its digits <= limit.
              - Ends with the given suffix.
            """
            num_length = len(num_str)
            suffix_length = len(suffix)
            
            # If the number has fewer digits than the suffix, no such number is possible.
            if num_length < suffix_length:
                return 0
            
            # If the number has the same length as the suffix, the only possible candidate is the number itself.
            if num_length == suffix_length:
                return 1 if num_str >= suffix else 0
            
            # Calculate the length of the prefix (the part before the suffix).
            prefix_length = num_length - suffix_length
            count = 0
            
            # Extract the actual suffix part of num_str.
            actual_suffix = num_str[prefix_length:]
            
            # Process each digit of the prefix from left to right.
            for i in range(prefix_length):
                # Calculate the number of ways to fill the remaining positions of the prefix after index i.
                ways_to_fill_rest = (limit + 1) ** (prefix_length - i - 1)
                current_digit = int(num_str[i])
                
                # If the current digit is greater than the allowed limit,
                # then any choice from 0 to limit is valid for this position.
                if current_digit > limit:
                    count += (limit + 1) * ways_to_fill_rest
                    return count
                
                # Count numbers formed by choosing a digit smaller than current_digit at this position
                # (which guarantees the entire number is less than num_str).
                count += current_digit * ways_to_fill_rest
            
            # If the prefix matches exactly the prefix of num_str, we need to check the suffix.
            # If the actual suffix is at least the required suffix, then num_str itself is valid.
            if actual_suffix >= suffix:
                count += 1
                
            return count

        # Count powerful integers between start and finish.
        return count_up_to(str(finish), suffix, limit) - count_up_to(str(start - 1), suffix, limit)

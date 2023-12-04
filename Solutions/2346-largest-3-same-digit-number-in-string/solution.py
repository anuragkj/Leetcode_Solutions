class Solution:
    def largestGoodInteger(self, num: str) -> str:
        same_digit_numbers = ["999", "888", "777", "666", "555", "444", "333", "222", "111", "000"]

        # Check whether the 'num' string contains the 'same_digit_number' string or not.
        def contains(same_digit_number):
            for index in range(len(num) - 2):
                if num[index] == same_digit_number[0] and \
                   num[index + 1] == same_digit_number[1] and \
                   num[index + 2] == same_digit_number[2]:
                    return True
            return False

        # Iterate on all 'same_digit_numbers' and check if the string 'num' contains it.
        for same_digit_number in same_digit_numbers:
            if contains(same_digit_number):
                # Return the current 'same_digit_number'.
                return same_digit_number
        # No 3 consecutive same digits are present in the string 'num'.
        return ""

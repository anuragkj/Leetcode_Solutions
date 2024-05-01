class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        stack = []
        result = []

        index = 0
        while index < len(word):
            stack.append(word[index])
            # Found ch
            if word[index] == ch:
                # Add characters through ch to the result in reverse order
                while stack:
                    result.append(stack.pop())
                index += 1
                # Add the rest of the characters to result
                while index < len(word):
                    result.append(word[index])
                    index += 1
                return ''.join(result)
            index += 1

        return word 

        

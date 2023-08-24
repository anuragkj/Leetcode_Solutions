class Solution:
    def fullJustify(self, words, maxWidth):
        result, cur, num_of_letters = [], [], 0

        for word in words:
            if num_of_letters + len(word) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i % (len(cur) - 1 or 1)] += ' '
                result.append(''.join(cur))
                cur, num_of_letters = [], 0

            cur += [word]
            num_of_letters += len(word)

        return result + [' '.join(cur).ljust(maxWidth)]

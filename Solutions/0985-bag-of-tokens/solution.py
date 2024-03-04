class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        low = 0
        high = len(tokens) - 1
        score = 0
        tokens.sort()

        while low <= high:
            # When we have enough power, play lowest token face-up
            if power >= tokens[low]:
                score += 1
                power -= tokens[low]
                low += 1

            # We don't have enough power to play a token face-up
            # If there is at least one token remaining,
            # and we have enough score, play highest token face-down
            elif low < high and score > 0:
                score -= 1
                power += tokens[high]
                high -= 1

            # We don't have enough score, power, or tokens 
            # to play face-up or down and increase our score
            else:
                return score

        return score       

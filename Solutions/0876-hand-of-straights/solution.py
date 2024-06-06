from collections import Counter
class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:


        if len(hand) % groupSize != 0:
            return False
        
        card_count = Counter(hand)
        sorted_cards = sorted(card_count)
        
        for card in sorted_cards:
            if card_count[card] > 0:  # there are still some of this card left to use
                count = card_count[card]
                for i in range(card, card + groupSize):
                    if card_count[i] < count:
                        return False
                    card_count[i] -= count

        return True

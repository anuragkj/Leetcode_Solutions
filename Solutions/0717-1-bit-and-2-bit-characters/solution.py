class Solution:
    def isOneBitCharacter(self, bits):
        i = 0
        while i < len(bits):
            if bits[i] == 1:
                i += 1
                if i == len(bits)-1:
                    return False
            i += 1
        return True

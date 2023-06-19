class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        net = 0
        curr = 0
        for i in gain:
            curr += i
            net = max(net, curr)
        return net

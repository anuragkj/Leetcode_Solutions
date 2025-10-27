from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        ans = 0
        prev = 0
        
        for row in bank:
            cnt = row.count('1')
            if cnt > 0:
                ans += prev * cnt
                prev = cnt
        return ans

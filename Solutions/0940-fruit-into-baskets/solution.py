class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        num1, frq1 = -1, 0
        num2, frq2 = -1, 0

        l = r = 0
        n = len(fruits)
        ans = 0

        while r < n:
            cur = fruits[r]

            if num1 == -1:
                num1 = cur
                frq1 = 1
            elif num1 == cur:
                frq1 += 1
            elif num2 == -1:
                num2 = cur
                frq2 = 1
            elif num2 == cur:
                frq2 += 1

            if cur != num1 and cur != num2:
                ans = max(frq1 + frq2, ans)

                last = fruits[r - 1]

                # empty bucket untill we have a free bucket
                while frq1 > 0 and frq2 > 0:
                    prev = fruits[l]

                    if prev == num1:
                        frq1 -= 1
                    elif prev == num2:
                        frq2 -= 1
                    l += 1

                # put new unique fruit in available empty bucket
                if frq1 == 0:
                    num1 = cur
                    frq1 = 1
                elif frq2 == 0:
                    num2 = cur
                    frq2 = 1

            r += 1

        ans = max(frq1 + frq2, ans)

        return ans

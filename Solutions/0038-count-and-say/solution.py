class Solution:
    def countAndSay(self, n: int) -> str:
        curr = "1"
        if n == 1:
            return curr
        for _ in range(2, n + 1):
            sb = []
            cnt = 1
            ele = curr[0]
            for j in range(1, len(curr)):
                if curr[j] == ele:
                    cnt += 1
                else:
                    sb.append(str(cnt))
                    sb.append(ele)
                    ele = curr[j]
                    cnt = 1
            sb.append(str(cnt))
            sb.append(ele)
            curr = ''.join(sb)
        return curr

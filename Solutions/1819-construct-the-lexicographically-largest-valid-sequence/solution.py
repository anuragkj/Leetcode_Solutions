class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        
        arr = [-1] * (2 * n - 1)
        used = [False for _ in range(n)]

        def dfs(idx):
            if all(used):
                return True
            if idx >= 2 * n - 1:
                return False
            if arr[idx] != -1:
                return dfs(idx + 1)

            for num in range(n - 1, -1, -1):
                if used[num] == True:
                    continue
                
                if num == 0:
                    used[num] = True
                    arr[idx] = 1
                    if dfs(idx + 1):
                        return True
                    used[num] = False
                    arr[idx] = -1
                    return False

                if idx + num + 1 >= 2 * n - 1:
                    return False
                if arr[idx + num + 1] != -1:
                    continue

                arr[idx] = num + 1  
                arr[idx + num + 1] = num + 1
                used[num] = True
                if dfs(idx + 1):
                    return True
                used[num] = False
                arr[idx + num + 1] = -1
            arr[idx] = -1
            return False

        dfs(0)
        return arr

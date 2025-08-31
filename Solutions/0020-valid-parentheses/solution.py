class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        dic = {
            '}':'{',
            ')':'(',
            ']':'['
        }

        for i in s:
            if i in dic.values():
                stack.append(i)
            if i in dic.keys():
                if len(stack) == 0: return False
                ele = stack.pop()
                if ele != dic[i]:
                    return False
        
        return True if len(stack)==0 else False
        
